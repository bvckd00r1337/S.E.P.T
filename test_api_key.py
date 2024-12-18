from backend.services.alpha_vantage_service import get_historical_data

symbol = 'AAPL'
data = get_historical_data(symbol)

if data:
    print("API Key is valid and data fetched successfully.")
else:
    print("Failed to fetch data. Check API key and rate limits.")
