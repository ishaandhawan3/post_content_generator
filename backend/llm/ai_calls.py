import openai
import os
from openai import AzureOpenAI
import logging
from config.logging_config import setup_logging

logger = logging.getLogger(__name__)

class LLMClient:
    