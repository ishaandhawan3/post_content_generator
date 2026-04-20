import os
from pathlib import Path
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        self.openai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def get_openai_client(self):
        return AzureOpenAI(
            api_key=self.openai_api_key,
            azure_endpoint=self.openai_api_base,
            api_version=self.openai_api_version,
        )
    
    def db_creds(self):
        return {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME")
        }


config = Config()
