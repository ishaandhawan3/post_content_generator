import logging
from fastapi import APIRouter, HTTPException
from services.generation import GenerationService

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
async def root():
    """
    This is the root endpoint
    """
    print("=========Welcome to Post generation engine=========")

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify that the API is running.
    Returns:
        dict: A dictionary containing the status of the API.
    """
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@router.post("/generate")
async def generate_content(topic: str | None = None, context: str | None = None, platform: str = "Linkedin"):
    """
    Endpoint to generate content based on the provided topic or context.
    Args:
        topic (str, optional): The topic for which to generate content. Defaults to None.
        context (str, optional): Additional context for content generation. Defaults to None.
        platform (str, optional): The social media platform for which to generate content. Defaults to "Linkedin".
    Returns:
        str: Generated content based on the input parameters.
    """
    topic = (topic or "").strip()
    context = (context or "").strip()
    platform = (platform or "").strip()

    if not platform:
        raise HTTPException(status_code=400, detail="Please provide a platform.")

    if topic:
        post_generator = GenerationService(topic=topic, platform=platform, context=context)
        generated_content = post_generator.generate_post_content()
        return {"content": generated_content}

    if context:
        topic_finder = GenerationService(topic=topic, platform=platform, context=context)
        trending_topics = topic_finder.find_trending_topics()
        return {"trending_topics": trending_topics}

    logger.error("Please provide either a topic or context for content generation.")
    raise HTTPException(status_code=400, detail="Please provide either a topic or context.")

    logger.info("Generate content endpoint called")
