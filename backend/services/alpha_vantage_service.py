import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_historical_data(symbol, interval='daily', outputsize='full'):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        print("API Key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")
        return None

    base_url = 'https://www.alphavantage.co/query'
    
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': outputsize,
        'apikey': api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'Error Message' in data:
            print(f"API Error for {symbol}: {data['Error Message']}")
            return None
        if 'Note' in data:
            print(f"API Note for {symbol}: {data['Note']}")
            return None
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed for {symbol}: {e}")
        return None