import json
import logging
from playwright.async_api import async_playwright
from config import *
from utils import fetch_with_retry, smart_delay

async def fetch_rv_data():
    """Main function to fetch RV data from the website"""
    logger = logging.getLogger(__name__)
    logger.info('Starting data fetch...')
    
    browser = None
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.connect_over_cdp(SBR_WS_CDP)
            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            
            # Lets just stat browser with home url
            # dummy_response = await fetch_with_retry(page, INITIAL_URL, "Initial data fetch", MAX_RETRIES)
            
            # page2 = await context.new_page()

            # Lets call the second API to get UNIT_IDS and PRODUCT_IDS
            response = await fetch_with_retry(page, SECOND_URL, "Secondary data fetch", MAX_RETRIES)
            json_data = json.loads(await response.text())
            total_units = len(json_data.get("Units", []))
            logger.info(f"Found {total_units} total units to process")
            
            # Process in chunks
            all_results = []
            
            # Add required fields to config payload
            config_payload = CONFIG_PAYLOAD.copy()
            config_payload["GlpForm"] = json.dumps({
                "formSnippetId": 231342, 
                "settings": [{"settingName": "FormType", "settingValue": "Unlock Your Price"}]
            })
            config_payload["GlpForceForm"] = json.dumps({
                "formSnippetId": 231342, 
                "settings": [{"settingName": "FormType", "settingValue": "Unlock Your Price"}]
            })
            
            for chunk_num in range(MAX_CHUNKS):
                start_idx = CHUNK_SIZE * chunk_num
                end_idx = min(start_idx + CHUNK_SIZE, total_units)
                
                if start_idx >= total_units:
                    break
                
                logger.info(f"Processing chunk {chunk_num + 1}/{MAX_CHUNKS} (units {start_idx} to {end_idx-1})")
                
                try:
                    units = json_data["Units"][start_idx:end_idx]
                    if not units:
                        continue
                    
                    # Prepare units payload
                    units_payload = [
                        {
                            "UnitId": str(unit["UnitId"]),
                            "Index": str(i + 1),
                            "TemplateName": "UnitListItemV2.cshtml",
                            "ProductId": str(unit["ProductId"]),
                            "ConsolidatedUnitIds": "null",
                            "ConsolidatedLotIds": "null"
                        }
                        for i, unit in enumerate(units) 
                        if "UnitId" in unit and "ProductId" in unit
                    ]
                    
                    if not units_payload:
                        continue
                    
                    # Make POST request with retry
                    for retry_attempt in range(MAX_RETRIES):
                        try:
                            result_json = await page.evaluate(
                                """async ({ units, config }) => {
                                    const formData = new FormData();
                                    formData.append("units", JSON.stringify(units));
                                    formData.append("config", JSON.stringify(config));
                                    const res = await fetch("https://www.bluecompassrv.com/rebraco/unitlist/getmultipleitemhtml", {
                                        method: "POST",
                                        body: formData
                                    });
                                    return await res.text();
                                }""",
                                {"units": units_payload, "config": config_payload}
                            )
                            
                            chunk_data = json.loads(result_json)
                            all_results.extend(chunk_data)
                            logger.info(f"Chunk {chunk_num + 1}: Successfully processed {len(chunk_data)} units")
                            break
                            
                        except (json.JSONDecodeError, Exception) as e:
                            logger.error(f"Chunk {chunk_num + 1}: Error on attempt {retry_attempt + 1}: {str(e)}")
                            if retry_attempt < MAX_RETRIES - 1:
                                await smart_delay()
                    
                    await smart_delay()
                    
                except Exception as e:
                    logger.error(f"Chunk {chunk_num + 1}: Unexpected error: {str(e)}")
                    continue
            
            logger.info(f"Completed processing. Total results: {len(all_results)}")
            return all_results
            
    except Exception as e:
        logger.error(f"Fatal error in fetch_rv_data: {str(e)}")
        raise
    finally:
        if browser:
            await browser.close()