import os

# Database configuration using environment variables for security
DB_HOST = os.getenv('DB_HOST', 'database-1.c122qawe6rs6.eu-north-1.rds.amazonaws.com')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('DB_NAME', 'database-1')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '234329Robert')

# ... existing code ... 