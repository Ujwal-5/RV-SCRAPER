import logging
from bs4 import BeautifulSoup
from typing import List, Dict
from utils import clean_price

def extract_rv_data(json_data: List[Dict]) -> tuple[List[Dict], List[Dict]]:
    """
    Extract RV data and separate into New and Used lists
    Returns: (new_rvs, used_rvs)
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Starting to extract data from {len(json_data)} items")
    
    new_rvs = []
    used_rvs = []
    
    for i, item in enumerate(json_data):
        try:
            if 'Html' not in item:
                continue
                
            soup = BeautifulSoup(item['Html'], 'html.parser')
            
            # Initialize data with required fields only
            rv_data = {
                'RV Type': '',
                'Stock No': '',
                'Price': '',
                'MSRP': '',
                'Location': '',
                'URL': ''
            }
            
            # Extract condition from title
            title_element = soup.find('a', href=lambda x: x and '/product/' in x)
            condition = ''
            if title_element:
                full_title = title_element.get_text().strip()
                condition = full_title.split()[0].lower() if full_title else ''
            
            # Skip if not New or Used
            if condition not in ['new', 'used']:
                continue
            
            # Extract Stock Number
            stock_element = soup.find('span', class_='stock-number-text')
            if stock_element:
                rv_data['Stock No'] = stock_element.get_text(strip=True)
            
            # Extract MSRP
            msrp_element = soup.find('span', class_='reg-price-text')
            if msrp_element:
                msrp_text = msrp_element.get_text(strip=True)
                rv_data['MSRP'] = clean_price(msrp_text) or ''
            
            # Extract Price, RV Type, and URL from container
            container = soup.find('div', class_='unit-content-wrapper')
            if container:
                # Get sale price
                sale_price = container.get('data-saleprice', '').replace('$', '').replace(',', '')
                msrp_attr = container.get('data-msrp', '').replace('$', '').replace(',', '')
                
                if sale_price and sale_price not in ['0.00', '0', '']:
                    rv_data['Price'] = f"${sale_price}"
                elif msrp_attr:
                    rv_data['Price'] = f"${msrp_attr}"
                
                # Get RV Type
                rv_type = container.get('data-type', '')
                if rv_type:
                    rv_data['RV Type'] = rv_type.title()
                
                # Get URL
                unit_link = container.get('data-unitlink', '')
                if unit_link:
                    rv_data['URL'] = f"https://www.bluecompassrv.com{unit_link}"
            
            # Extract Location
            location_element = soup.find('span', class_='unit-location-text')
            if location_element:
                rv_data['Location'] = location_element.get_text(strip=True)
            
            # Only add if we have essential data
            if rv_data['Stock No'] and rv_data['Price']:
                if condition == 'new':
                    new_rvs.append(rv_data)
                elif condition == 'used':
                    used_rvs.append(rv_data)
                
        except Exception as e:
            logger.error(f"Error processing item {i}: {str(e)}")
            continue
    
    logger.info(f"Successfully extracted {len(new_rvs)} new and {len(used_rvs)} used RVs")
    return new_rvs, used_rvs