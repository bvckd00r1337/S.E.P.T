# backend/app.py

from dotenv import load_dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from services.alpha_vantage_service import get_historical_data
from scheduler import scheduler  # Ensure this import is uncommented and scheduler is properly defined

# Initialize SQLAlchemy
db = SQLAlchemy()

# Load environment variables from the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

database_url = os.getenv('DATABASE_URL')
print(f"DATABASE_URL: {database_url}")  # Debugging line

def create_app():
    app = Flask(__name__)
    
    # Debugging: Check Flask version and app attributes
    import flask
    print(f"Flask Version: {flask.__version__}")
    print("Available attributes in app:", dir(app))
    print("Has before_first_request:", hasattr(app, 'before_first_request'))

    # Configure the SQLAlchemy part of the app instance
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the app with the SQLAlchemy db
    db.init_app(app)

    # Import models after initializing db to avoid circular imports
    from models import Stock  # Ensure this line is uncommented if models are defined

    # Import scheduler after app and db are initialized
    # from scheduler import scheduler  # Already imported above

    @app.route('/fetch-data/<symbol>')
    def fetch_data(symbol):
        fetch_and_store_stock_data(symbol)
        return f"Data fetching initiated for {symbol}" 

    def fetch_and_store_stock_data(symbol):
        try:
            data = get_historical_data(symbol, interval='daily', outputsize='full')
            store_data_in_db(symbol, data)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

    def store_data_in_db(symbol, data):
        """
        Stores historical stock data into the database.

        :param symbol: Stock ticker symbol
        :param data: JSON data from Alpha Vantage
        """
        try:
            time_series_key = next(key for key in data.keys() if 'Time Series' in key)
            time_series = data[time_series_key]

            for date_str, metrics in time_series.items():
                stock = Stock(
                    symbol=symbol,
                    date=datetime.strptime(date_str, '%Y-%m-%d').date(),
                    open=metrics['1. open'],
                    high=metrics['2. high'],
                    low=metrics['3. low'],
                    close=metrics['4. close'],
                    volume=metrics['5. volume']
                )
                db.session.add(stock)

            db.session.commit()
            print(f"Successfully stored data for {symbol}")
        except Exception as e:
            db.session.rollback()
            print(f"Error storing data for {symbol}: {e}")

    with app.app_context():
        db.create_all()
        # Start the scheduler within the app context
        if not scheduler.running:
            scheduler.start()
            print("Scheduler started.")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)