import os
import csv
import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("fetch_symbols.log"),
        logging.StreamHandler()
    ]
)

# URLs for symbol directories
NASDAQ_LISTED_URL = "http://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_LISTED_URL = "http://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"

# Output CSV file paths
NASDAQ_CSV = os.path.join(os.path.dirname(__file__), '../../data/nasdaq_symbols.csv')
NYSE_CSV = os.path.join(os.path.dirname(__file__), '../../data/nyse_symbols.csv')


def download_symbol_file(url):
    """
    Downloads the symbol directory file from the given URL.
    Returns the content as a string.
    """
    try:
        logging.info(f"Downloading symbol file from {url}")
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Download successful.")
        return response.text
    except requests.HTTPError as http_err:
        logging.error(f"HTTP error occurred while downloading {url}: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred while downloading {url}: {err}")
    return None


def parse_nasdaq_listed(data):
    """
    Parses NASDAQ listed symbols from the downloaded data.
    Returns a list of dictionaries with 'Symbol' and 'Security Name'.
    """
    symbols = []
    lines = data.strip().split('\n')
    header = lines[0].split('|')
    for line in lines[1:]:
        if line.startswith('File Creation Time'):
            break
        parts = line.split('|')
        symbol = parts[0]
        security_name = parts[1]
        symbols.append({'Symbol': symbol, 'Security Name': security_name})
    logging.info(f"Parsed {len(symbols)} NASDAQ symbols.")
    return symbols


def parse_other_listed(data):
    """
    Parses other listed symbols (e.g., NYSE) from the downloaded data.
    Returns a list of dictionaries with 'ACT Symbol' and 'Security Name'.
    """
    symbols = []
    lines = data.strip().split('\n')
    header = lines[0].split('|')
    for line in lines[1:]:
        if line.startswith('File Creation Time'):
            break
        parts = line.split('|')
        exchange = parts[4]
        if exchange.upper() == 'NYSE':  # NYSE Symbol
            symbol = parts[0]
            security_name = parts[1]
            symbols.append({'Symbol': symbol, 'Security Name': security_name})
    logging.info(f"Parsed {len(symbols)} NYSE symbols.")
    return symbols


def save_to_csv(symbols, filepath):
    """
    Saves the list of symbol dictionaries to a CSV file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Symbol', 'Security Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for symbol in symbols:
                writer.writerow(symbol)
        logging.info(f"Saved {len(symbols)} symbols to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save symbols to {filepath}: {e}")


def fetch_and_save_symbols():
    # Fetch NASDAQ listed symbols
    nasdaq_data = download_symbol_file(NASDAQ_LISTED_URL)
    if nasdaq_data:
        nasdaq_symbols = parse_nasdaq_listed(nasdaq_data)
        save_to_csv(nasdaq_symbols, NASDAQ_CSV)

    # Fetch other listed symbols (e.g., NYSE)
    other_data = download_symbol_file(OTHER_LISTED_URL)
    if other_data:
        nyse_symbols = parse_other_listed(other_data)
        save_to_csv(nyse_symbols, NYSE_CSV)


if __name__ == "__main__":
    fetch_and_save_symbols()