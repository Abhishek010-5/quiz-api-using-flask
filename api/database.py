from pymongo import MongoClient
from api.config import DB_URI, DB

def connect_database():
    try:
        client = MongoClient(DB_URI)
        db = client[DB]
        # Optional: Verify connection
        db.command('ping')  # This will raise an exception if connection fails
        return db
    except Exception as e:
        return f"Database connection error: {str(e)}"