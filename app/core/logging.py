import logging
import uuid
from fastapi import Request

logger = logging.getLogger("onboarding")
logging.basicConfig(level=logging.INFO)


async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    logger.info(f"Request {request_id} started: {request.url}")
    response = await call_next(request)
    logger.info(f"Request {request_id} completed")
    return response