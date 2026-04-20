import os
import dotenv
from config import Config

dotenv.load_dotenv()

db_url = os.getenv("DATABASE_URL")

class Database:
    def __init__(self):
        self.url = db_url
    
    def connect(self):
        # Placeholder for database connection logic
        print(f"Connecting to database at {self.url}")
    
    def disconnect(self):
        # Placeholder for database disconnection logic
        print("Disconnecting from database")
    
    def execute_query(self, query):
        # Placeholder for query execution logic
        print(f"Executing query: {query}")
