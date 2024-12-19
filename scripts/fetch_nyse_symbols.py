import os
import csv
import logging
import pandas as pd
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("fetch_nyse_symbols.log"),
        logging.StreamHandler()
    ]
)

# Wikipedia URL containing NYSE-listed companies
WIKIPEDIA_NYSE_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_100_companies"

# Output CSV file path
NYSE_OUTPUT_CSV = os.path.join(os.path.dirname(__file__), '../../data/nyse_symbols.csv')


def fetch_wikipedia_page(url):
    """
    Fetches the content of the Wikipedia page.
    Returns the HTML content if successful, else None.
    """
    try:
        logging.info(f"Fetching Wikipedia page from {url}")
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Wikipedia page fetched successfully.")
        return response.text
    except requests.HTTPError as http_err:
        logging.error(f"HTTP error occurred while fetching {url}: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred while fetching {url}: {err}")
    return None


def parse_nyse_symbols(html_content):
    """
    Parses the HTML content to extract NYSE symbols and their security names.
    Removes duplicates based on the 'Symbol' field.
    Returns a list of unique dictionaries with 'Symbol' and 'Security Name'.
    """
    symbols = []
    try:
        logging.info("Parsing NYSE symbols from the Wikipedia page.")
        tables = pd.read_html(html_content)
        
        # Identify the correct table containing NYSE symbols
        # This may vary; adjust the index or implement logic to find the right table
        # For demonstration, we'll assume the table containing 'Symbol' and 'Security' columns is the correct one
        target_table = None
        for table in tables:
            if {'Symbol', 'Security'}.issubset(table.columns):
                target_table = table
                break
        
        if target_table is None:
            logging.error("No suitable table found on the Wikipedia page.")
            return symbols
        
        # Drop duplicates based on 'Symbol'
        initial_count = len(target_table)
        target_table.drop_duplicates(subset=['Symbol'], inplace=True)
        final_count = len(target_table)
        duplicates_removed = initial_count - final_count
        if duplicates_removed > 0:
            logging.info(f"Removed {duplicates_removed} duplicate symbols.")
        
        # Extract 'Symbol' and 'Security Name'
        for index, row in target_table.iterrows():
            symbol = str(row['Symbol']).strip()
            security_name = str(row['Security']).strip()
            if symbol and security_name:
                symbols.append({'Symbol': symbol, 'Security Name': security_name})
        
        logging.info(f"Parsed {len(symbols)} unique NYSE symbols from the table.")
    except ValueError as ve:
        logging.error(f"Value error during parsing: {ve}")
    except Exception as e:
        logging.error(f"An error occurred while parsing NYSE symbols: {e}")
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
        logging.info(f"Saved {len(symbols)} unique NYSE symbols to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save symbols to {filepath}: {e}")


def fetch_nyse_symbols():
    """
    Orchestrates the fetching and saving of NYSE symbols from Wikipedia.
    """
    html_content = fetch_wikipedia_page(WIKIPEDIA_NYSE_URL)
    if html_content:
        nyse_symbols = parse_nyse_symbols(html_content)
        if nyse_symbols:
            save_to_csv(nyse_symbols, NYSE_OUTPUT_CSV)
        else:
            logging.error("No NYSE symbols were parsed.")
    else:
        logging.error("Failed to fetch the Wikipedia page.")


if __name__ == "__main__":
    fetch_nyse_symbols()