import logging
from config import config
import json
from config.config import config
from llm.prompt import Prompts

logger = logging.getLogger(__name__)

class GenerationService:
    def __init__(self, topic: str = "", platform: str = "", context: str = ""):
        self.config = config
        self.openai_client = self.config.get_openai_client()
        self.topic = topic
        self.platform = platform
        self.context = context
    
    
    def generate_post_content(self) -> str:
        """
        Generates post content based on the given topic using OpenAI's API.
        Args:
            topic (str): The topic for which to generate post content.
            platform (str): The social media platform for which to generate content.
        Returns:
            str: The generated post content.
        """
        logger.info("Content Generation started...")
        try:
            client = self.openai_client
            prompt_object = Prompts(topic=self.topic, platform=self.platform, context=self.context)
            result = client.chat.completions.create(
                model = self.config.openai_deployment_name,
                messages = [
                    {
                        "role": "system",
                        "content": prompt_object.get_content_prompt()
                    }
                ]
            )
            content = result.choices[0].message.content.strip()
            logger.info("Content Generated!!")
            logger.info(content)
            return content
        except Exception as e:
            logger.error(f"Error generating post content: {e}")
            return "Sorry, I couldn't generate the post content at this time."
    
    def find_trending_topics(self):
        """
        Finds trending topics based on the given context using OpenAI's API.
        Args:
            context (str): The context for which to find trending topics.
        Returns:
            list: A list of trending topics.
        """
        logger.info("Finding Trending Topics...")
        try:
            client = self.openai_client
            prompt_object = Prompts(topic=self.topic, platform=self.platform, context=self.context)
            result = client.chat.completions.create(
                model = self.config.openai_deployment_name,
                messages = [
                    {
                        "role": "system",
                        "content": prompt_object.get_topic_finder_prompt()
                    }
                ]
            )
            response_content = result.choices[0].message.content.strip()
            trending_topics = json.loads(response_content).get("trending_topics", [])
            logger.info("Topics found :: \n", trending_topics)
            return trending_topics
        except Exception as e:
            logger.error(f"Error finding trending topics: {e}")
            return ["Sorry, I couldn't find trending topics at this time."]
        
