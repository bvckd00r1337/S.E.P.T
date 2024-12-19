import dbdata
import psycopg2
from psycopg2 import OperationalError
import os

# Database configuration using environment variables for security
DB_HOST = os.getenv('DB_HOST', 'database-1.c122qawe6rs6.eu-north-1.rds.amazonaws.com')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('DB_NAME', 'database-1')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '234329Robert')
def create_aws_connection():
    try:
        connection = psycopg2.connect(
            host=dbdata.DB_HOST,
            port=dbdata.DB_PORT,
            database=dbdata.DB_NAME,
            user=dbdata.DB_USER,
            password=dbdata.DB_PASSWORD,
            sslmode='require'  # Ensures SSL connection for security
        )
        print("Connected to AWS RDS PostgreSQL database successfully.")
        return connection
    except OperationalError as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    conn = create_aws_connection()
    if conn:
        # Perform database operations
        conn.close()
        print("PostgreSQL connection closed.")