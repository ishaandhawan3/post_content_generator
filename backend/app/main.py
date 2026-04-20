import uuid
import time
from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
from config.logging_config import setup_logging, request_id_ctx_var
from config.config import config
from api.routes import router

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Post Content Generator API",
    description="API for generating social media post content based on topics and trends using OpenAI's API.",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.middleware("http")
async def log_request_session(request: Request, next_call):
    # Generate a unique session ID for this request
    request_id = str(uuid.uuid4())
    token = request_id_ctx_var.set(request_id)

    start_time = time.time()
    response = await next_call(request)
    process_time = time.time() - start_time

    #log the request details along with the session ID and processing time
    logger.info(f"HTTP Request: {request.method} {request.url} completed in {process_time:.2f}ms")

    # Reset the context variable to avoid leaking session ID to other requests
    request_id_ctx_var.reset(token)
    return response

if __name__ == "__main__":
    logger.info("=======Post Content Generation API========")

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9001)

