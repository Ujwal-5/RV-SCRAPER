import csv
import logging
from datetime import datetime
from typing import List, Dict
from config import CSV_FIELDS

def save_to_csv(new_rvs: List[Dict], used_rvs: List[Dict]):
    """Save New and Used RVs to separate CSV files"""
    logger = logging.getLogger(__name__)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save New RVs
    if new_rvs:
        new_filename = f"rv_new_{timestamp}.csv"
        with open(new_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(new_rvs)
        logger.info(f"Saved {len(new_rvs)} new RVs to {new_filename}")
    else:
        logger.warning("No new RVs to save")
    
    # Save Used RVs
    if used_rvs:
        used_filename = f"rv_used_{timestamp}.csv"
        with open(used_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(used_rvs)
        logger.info(f"Saved {len(used_rvs)} used RVs to {used_filename}")
    else:
        logger.warning("No used RVs to save")
    
    return len(new_rvs), len(used_rvs)