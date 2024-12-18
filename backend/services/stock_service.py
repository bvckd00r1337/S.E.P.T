import os
import sys
from datetime import datetime
import logging
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from alpha_vantage_service import get_historical_data
from models import Stocks
from database import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def fetch_and_store_stock_data(symbol):
    logging.info(f"Fetching data for symbol: {symbol}")
    data = get_historical_data(symbol)
    if not data:
        logging.error("No data retrieved.")
        return
    logging.info("Data fetched successfully.")
    store_data_in_db(symbol, data)

def store_data_in_db(symbol, data):
    logging.info("Storing data in the database.")
    time_series_key = 'Time Series (Daily)'
    time_series = data.get(time_series_key, {})
    if not time_series:
        logging.error(f"No '{time_series_key}' found in data for symbol: {symbol}")
        return

    session = Session()
    records_added = 0
    try:
        for date_str, metrics in time_series.items():
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                existing = session.query(Stocks).filter_by(symbol=symbol, date=date).first()
                if existing:
                    continue

                stock = Stocks(
                    symbol=symbol,
                    date=date,
                    open=metrics.get('1. open'),
                    high=metrics.get('2. high'),
                    low=metrics.get('3. low'),
                    close=metrics.get('4. close'),
                    volume=metrics.get('5. volume')
                )
                session.add(stock)
                records_added += 1
            except Exception as e:
                logging.error(f"Error processing {date_str} for {symbol}: {e}")
        session.commit()
        logging.info(f"Successfully stored {records_added} new records for {symbol}.")
    except IntegrityError:
        session.rollback()
        logging.error("Integrity Error: Likely duplicate entries.")
    except Exception as e:
        session.rollback()
        logging.error(f"Error storing data for {symbol}: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m services.stock_service <STOCK_SYMBOL>")
    else:
        symbol = sys.argv[1].upper()
        fetch_and_store_stock_data(symbol) 