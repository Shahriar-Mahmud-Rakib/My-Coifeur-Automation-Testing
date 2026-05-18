import os
import psycopg2
from psycopg2 import sql

# Database Configuration (From User Setup)
DB_HOST = os.getenv("DATABASE_HOST", "52.220.54.42")
DB_PORT = os.getenv("DATABASE_PORT", "5432")
DB_NAME = os.getenv("DATABASE_NAME", "mycoifeur_dev_db")
DB_USER = os.getenv("DATABASE_USERNAME", "mycoifeur_dev_user")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "gY2TDhhC3vBCeNN7SZQc")

def get_db_connection():
    """Establish and return a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def get_otp(identifier: str) -> str:
    """
    Fetch the latest OTP for a given email or phone number.
    NOTE: Update the table and column names below to match the actual database schema.
    """
    conn = get_db_connection()
    if not conn:
        return "123456"  # Fallback to bypass code if DB is unreachable

    try:
        cursor = conn.cursor()
        
        # Example Query 1: If OTP is stored in a dedicated otp_codes table
        # query = "SELECT code FROM otp_codes WHERE phone = %s OR email = %s ORDER BY created_at DESC LIMIT 1;"
        
        # Query OTP from users table using the reset_code column
        query = "SELECT reset_code FROM users WHERE phone = %s OR email = %s LIMIT 1;"
        
        cursor.execute(query, (identifier, identifier))
        result = cursor.fetchone()
        
        if result and result[0]:
            return str(result[0])
        else:
            print(f"No OTP found for {identifier} in database. Falling back to default.")
            return "123456"
            
    except Exception as e:
        print(f"Database query error: {e}")
        return "123456"
        
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Quick test when running the file directly
    test_identifier = "user1@gmail.com"
    otp = get_otp(test_identifier)
    print(f"Test OTP for {test_identifier}: {otp}")
