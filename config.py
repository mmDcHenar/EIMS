from decouple import config
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = config("DATABASE_URL", cast=str, default="sqlite:///db.sqlite3")
