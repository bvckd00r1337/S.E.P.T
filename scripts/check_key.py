import os

api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
if api_key:
    print("API Key is set.")
else:
    print("API Key is NOT set.")
