from apscheduler.schedulers.background import BackgroundScheduler
from services.stock_service import fetch_and_store_stock_data

scheduler = BackgroundScheduler()

# Example job: Fetch data every day at midnight
scheduler.add_job(func=fetch_and_store_stock_data, trigger="interval", days=1, args=["AAPL"])

scheduler.start() 