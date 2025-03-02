from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_URI = os.getenv("URI")
DB = os.getenv("DB")
SECRET_KEY = os.getenv("SECRET_KEY")