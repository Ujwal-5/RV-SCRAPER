# Configuration settings for RV scraper

# Browser authentication
AUTH = 'brd-customer-hl_c7826fc5-zone-scraping_browser1:ndeuvclk1i4t'
SBR_WS_CDP = f'wss://{AUTH}@brd.superproxy.io:9222'

# Scraping settings
MAX_RETRIES = 3
BASE_DELAY = 2
CHUNK_SIZE = 1000
MAX_CHUNKS = 20
TOTAL_FILES = 19572

# URLs
INITIAL_URL = "https://www.bluecompassrv.com/rv-search?pagesize=1"

SECOND_URL = f"https://www.bluecompassrv.com/rebraco/unitlist/results?pagesize={TOTAL_FILES}&criteria=%7B%22HideLibrary%22%3Atrue%2C%22OnlyLibrary%22%3Afalse%2C%22UnitAgeFilter%22%3A0%2C%22InvertTagFilter%22%3Afalse%2C%22InvertTypeFilter%22%3Afalse%2C%22StatusId%22%3A%222%2C5%22%2C%22InvertManufacturerFilter%22%3Afalse%2C%22Year%22%3A%222025%7C2025%2C2020%7C2024%2C2015%7C2019%2C0%7C2014%2C%2C2026%7C2026%22%2C%22PriceFilters%22%3A%5B%5D%2C%22MonthlyPaymentsFilters%22%3A%5B%5D%2C%22PropVals%22%3A%7B%7D%2C%22ResultsSortString%22%3A%22status-asc%2Cdistance-asc%2Ccondition-desc%2Cprice-asc%22%2C%22PageSize%22%3A100%2C%22PageNum%22%3A0%2C%22NoResultsPredetermined%22%3Afalse%2C%22IsCompact%22%3Afalse%7D&config=%7B%22PageId%22%3A231333%2C%22GlpForm%22%3A%22%7B%5Cn++%5C%22formSnippetId%5C%22%3A+231342%2C%5Cn++%5C%22settings%5C%22%3A+%5B%5Cn++++%7B%5Cn++++++%5C%22settingName%5C%22%3A+%5C%22FormType%5C%22%2C%5Cn++++++%5C%22settingValue%5C%22%3A+%5C%22Unlock+Your+Price%5C%22%5Cn++++%7D%5Cn++%5D%5Cn%7D%22%2C%22GlpForceForm%22%3A%22%7B%5Cn++%5C%22formSnippetId%5C%22%3A+231342%2C%5Cn++%5C%22settings%5C%22%3A+%5B%5Cn++++%7B%5Cn++++++%5C%22settingName%5C%22%3A+%5C%22FormType%5C%22%2C%5Cn++++++%5C%22settingValue%5C%22%3A+%5C%22Unlock+Your+Price%5C%22%5Cn++++%7D%5Cn++%5D%5Cn%7D%22%2C%22GlpNoPriceConfirm%22%3A231330%2C%22GlpPriceConfirm%22%3A1436%2C%22Slider%22%3Afalse%2C%22SliderPaused%22%3Afalse%2C%22VertSlider%22%3Afalse%2C%22VisibleSlides%22%3A3%2C%22IsCompact%22%3Afalse%2C%22Limit%22%3A0%2C%22SearchMode%22%3Afalse%2C%22DefaultSortMode%22%3A%22status-asc%2Cdistance-asc%2Ccondition-desc%2Cprice-asc%22%2C%22UseFqdnUnitLinks%22%3Afalse%2C%22NumberOfSoldIfNoActive%22%3A0%2C%22NoResultsSnippetId%22%3A0%2C%22ShowSimilarUnitsIfNoResults%22%3Afalse%2C%22DefaultPageSize%22%3A100%2C%22ImageWidth%22%3A400%2C%22ImageHeight%22%3A0%2C%22NoPriceText%22%3A%22Call+for+Price!%22%2C%22ShowPaymentsAround%22%3Afalse%2C%22ShowPaymentsAroundInCompactMode%22%3Afalse%2C%22DefaultToGridMode%22%3Afalse%2C%22DisableAjax%22%3Afalse%2C%22PriceTooltip%22%3A%22%22%2C%22FavoritesMode%22%3Afalse%2C%22ConsolidatedMode%22%3Afalse%7D"

POST_URL = "https://www.bluecompassrv.com/rebraco/unitlist/getmultipleitemhtml"

# POST payload configuration
CONFIG_PAYLOAD = {
    "PageId": 231333,
    "GlpNoPriceConfirm": 231330,
    "GlpPriceConfirm": 1436,
    "Slider": False,
    "SliderPaused": False,
    "VertSlider": False,
    "VisibleSlides": 3,
    "IsCompact": False,
    "Limit": 0,
    "SearchMode": False,
    "DefaultSortMode": "status-asc,distance-asc,condition-desc,price-asc",
    "UseFqdnUnitLinks": False,
    "NumberOfSoldIfNoActive": 0,
    "NoResultsSnippetId": 0,
    "ShowSimilarUnitsIfNoResults": False,
    "DefaultPageSize": 100,
    "ImageWidth": 400,
    "ImageHeight": 0,
    "NoPriceText": "Call for Price!",
    "ShowPaymentsAround": False,
    "ShowPaymentsAroundInCompactMode": False,
    "DefaultToGridMode": False,
    "DisableAjax": False,
    "PriceTooltip": "",
    "FavoritesMode": False,
    "ConsolidatedMode": False
}

# CSV field names
CSV_FIELDS = ["RV Type", "Stock No", "Price", "MSRP", "Location", "URL"]