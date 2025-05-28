# RV Scraper - Blue Compass RV Data Extractor

A Python-based web scraper that extracts RV listings from Blue Compass RV website, separating new and used vehicles into organized CSV files.

## 🚀 Features

- **Automated Data Extraction**: Scrapes RV listings including type, stock number, price, MSRP, location, and URL
- **Smart Categorization**: Automatically separates new and used RVs into different CSV files
- **Chunked Processing**: Handles large datasets (19,000+ listings) through intelligent chunking
- **Retry Logic**: Built-in error handling with configurable retry attempts
- **Browser Automation**: Uses Playwright with proxy support for reliable scraping
- **Comprehensive Logging**: Detailed logging with timestamps for monitoring and debugging

## 📋 Requirements

```
Python 3.8+
playwright
beautifulsoup4
nest-asyncio
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Ujwal-5/RV-SCRAPER.git
cd rv-scraper
```

2. Install dependencies:
```bash
pip install playwright beautifulsoup4 nest-asyncio
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## ⚙️ Configuration

The scraper is configured through `config.py`:

- **Browser Settings**: Proxy authentication and connection details
- **Scraping Parameters**: Chunk size (1000), max chunks (20), retry attempts (3)
- **Target Data**: Total files (~19,572 RV listings)
- **Output Format**: CSV with fields: RV Type, Stock No, Price, MSRP, Location, URL

## 🏃‍♂️ Usage

Run the scraper:
```bash
python main.py
```

The scraper will:
1. Connect to Blue Compass RV website
2. Fetch all available RV listings
3. Process data in chunks of 1000 units
4. Extract and categorize RV information
5. Save results to timestamped CSV files

## 📁 Project Structure

```
├── main.py           # Main orchestration script
├── config.py         # Configuration settings
├── fetcher.py        # Data fetching logic with Playwright
├── extractor.py      # HTML parsing and data extraction
├── saver.py          # CSV file generation
├── utils.py          # Utility functions (logging, delays, retries)
└── logs/             # Generated log files
```

## 📊 Output Files

The scraper generates timestamped CSV files:
- `rv_new_YYYYMMDD_HHMMSS.csv` - New RV listings
- `rv_used_YYYYMMDD_HHMMSS.csv` - Used RV listings

### CSV Structure
| Field | Description |
|-------|-------------|
| RV Type | Vehicle category (Travel Trailer, Motorhome, etc.) |
| Stock No | Dealer stock number |
| Price | Current selling price |
| MSRP | Manufacturer's suggested retail price |
| Location | Dealer location (City, State) |
| URL | Direct link to listing |

## 📝 Logging

All operations are logged with timestamps to:
- Console output for real-time monitoring
- Log files in `logs/` directory for detailed analysis

Log levels include:
- **INFO**: Successful operations and progress updates
- **WARNING**: Non-critical issues
- **ERROR**: Failed operations with retry attempts

## 🔧 Configuration Options

Key settings in `config.py`:

```python
MAX_RETRIES = 3        # Retry attempts for failed requests
BASE_DELAY = 2         # Base delay between requests (seconds)
CHUNK_SIZE = 1000      # Items processed per chunk
MAX_CHUNKS = 20        # Maximum chunks to process
```

## 🚨 Error Handling

The scraper includes robust error handling:
- **Connection Issues**: Automatic retry with exponential backoff
- **Browser Crashes**: Graceful recovery and continuation
- **Data Parsing Errors**: Skip invalid entries and continue processing
- **Rate Limiting**: Smart delays between requests

## 📈 Performance

- **Processing Speed**: ~1,000 listings per 1-3 minutes
- **Memory Efficient**: Chunked processing prevents memory overflow
- **Network Resilient**: Handles temporary network issues gracefully

## 🔍 Recent Run Summary

**Last Successful Run**: May 28, 2025 09:10-09:43 (33 minutes)

**Results**:
- **Total Units Processed**: 14,000 out of 19,572 available
- **New RVs Extracted**: 12,305
- **Used RVs Extracted**: 1,695
- **Success Rate**: ~71.5% (14/20 chunks completed)

**Issues Encountered**:
- Browser connection closed after chunk 14
- Chunks 15-20 failed due to connection issues
- Partial data recovery successful

## 🔮 Future Improvements

- [ ] Implement browser reconnection for failed chunks
- [ ] Add resume functionality from last successful chunk
- [ ] Include additional RV details (year, make, model)
- [ ] Add data validation and quality checks

