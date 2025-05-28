import asyncio
import nest_asyncio
from utils import setup_logging
from fetcher import fetch_rv_data
from extractor import extract_rv_data
from saver import save_to_csv

# Apply nest_asyncio to handle nested event loops
nest_asyncio.apply()

async def main():
    """Main function to orchestrate the RV scraping process"""
    logger = setup_logging()
    logger.info("=== RV Scraper Starting ===")
    
    try:
        # Fetch raw data
        logger.info("Fetching RV data...")
        raw_data = await fetch_rv_data()
        
        if not raw_data:
            logger.error("No data fetched, exiting")
            return
        
        # Extract and separate New/Used RVs
        logger.info("Extracting and processing RV data...")
        new_rvs, used_rvs = extract_rv_data(raw_data)
        
        if not new_rvs and not used_rvs:
            logger.error("No valid RV data extracted, exiting")
            return
        
        # Save to CSV files
        logger.info("Saving data to CSV files...")
        new_count, used_count = save_to_csv(new_rvs, used_rvs)
        
        # Final summary
        logger.info("=== RV Scraper Completed Successfully ===")
        logger.info(f"New RVs: {new_count}")
        logger.info(f"Used RVs: {used_count}")
        logger.info(f"Total: {new_count + used_count}")
        
        # Show sample data
        if new_rvs:
            logger.info(f"Sample New RV: {new_rvs[0]}")
        if used_rvs:
            logger.info(f"Sample Used RV: {used_rvs[0]}")
        
    except KeyboardInterrupt:
        logger.info("Scraper interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScraper stopped by user")
    except Exception as e:
        print(f"Scraper failed: {str(e)}")