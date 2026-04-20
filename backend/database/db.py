import os
import dotenv
import psycopg2
from config.config import Config
from config.logging_config import setup_logging

dotenv.load_dotenv()

db_url = os.getenv("DATABASE_URL")

class Database:

    try:
        connection = psycopg2.connect(
                    user = Config().db_creds()["user"],
                    password = Config().db_creds()["password"],
                    host = Config().db_creds()["host"],
                    port = Config().db_creds()["port"],
                    database = Config().db_creds()["database"]
                )
    except Exception as e:
        print(f"Error connecting to database: {e}")

    
    def connect(self):
        # Placeholder for database connection logic
        print(f"Connecting to database at {db_url}")
        connection = psycopg2.connect(db_url)
        return connection

    def disconnect(self):
        # Placeholder for database disconnection logic
        print("Disconnecting from database")
        self.connection.close()
        print("Disconnected from database")
    
    def execute_query(self, query):
        # Placeholder for query execution logic
        print(f"Executing query: {query}")
        cursor = self.connection.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        print(f"Query result: {record}")
        return record

