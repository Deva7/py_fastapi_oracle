import oracledb, os
from dotenv import load_dotenv

load_dotenv()

# Database connection details
db_config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dsn": os.getenv("DB_DSN")
}

# Connect to the Oracle database
def get_db_connection():
   return oracledb.connect(user=os.getenv("DB_USER"),
                           password=os.getenv("DB_PASSWORD"),
                           dsn=os.getenv("DB_DSN"))