# import os
# import logging
# from config.config import config

# logger = logging.getLogger(__name__)

# class TopicSearch:
#     def __init__(self, context: str):
#         self.context = context
    
# pip install duckduckgo_search
from ddgs import DDGS

def search_entire_web(query: str = ""):
    with DDGS() as ddgs:
        return [r for r in ddgs.text(query, max_results=5)]

if __name__ == "__main__":
    context = "Machine Learning"
    query = f"Give me trending topics to write posts on {context}"
    print(search_entire_web(query))
