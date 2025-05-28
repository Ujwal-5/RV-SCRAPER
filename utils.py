import re
import logging
import random
import asyncio
from datetime import datetime
from typing import Optional
from config import BASE_DELAY

def setup_logging():
    """Setup logging configuration"""
    log_filename = f"logs/rv_scraper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler(log_filename), logging.StreamHandler()]
    )
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized. Log file: {log_filename}")
    return logger

def clean_price(price_str: str) -> Optional[str]:
    """Clean price string and return formatted price"""
    if not price_str or price_str.lower() in ['call for price!', 'call for price', '']:
        return None
    
    # Remove everything except digits, periods, and commas
    cleaned = re.sub(r'[^\d,.]', '', price_str).replace(',', '')
    try:
        price_float = float(cleaned)
        return f"${int(price_float)}"  # Return as $12345 format
    except (ValueError, TypeError):
        return None

async def smart_delay():
    """Add random delay between requests"""
    delay = random.uniform(BASE_DELAY, BASE_DELAY * 2)
    await asyncio.sleep(delay)

async def fetch_with_retry(page, url: str, operation_name: str, max_retries: int):
    """Fetch data with retry logic"""
    logger = logging.getLogger(__name__)
    
    for attempt in range(max_retries):
        try:
            logger.info(f"{operation_name} - Attempt {attempt + 1}/{max_retries}")
            response = await page.goto(url, timeout=60000)
            if response.status == 200:
                logger.info(f"{operation_name} successful")
                return response
            else:
                logger.warning(f"{operation_name} - HTTP {response.status}")
        except Exception as e:
            logger.error(f"{operation_name} - Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                delay = min(BASE_DELAY * (2 ** attempt) + random.uniform(0, 1), 30)
                await asyncio.sleep(delay)
            else:
                raise e