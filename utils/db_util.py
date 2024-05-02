import os
from dotenv import load_dotenv

class DBConfig:
    @staticmethod
    def load():
        load_dotenv()
        print("hellow")
        return {
            "DATABASE_NAME": os.getenv("DB_NAME"),
            "DATABASE_USER": os.getenv("DB_USER"),
            "DATABASE_PASSWORD": os.getenv("DB_PASSWORD"),
            "DATABASE_HOST": os.getenv("DB_HOST"),
            "DATABASE_PORT": os.getenv("DB_PORT")
        }

# Usage:
db_config = DBConfig.load()

