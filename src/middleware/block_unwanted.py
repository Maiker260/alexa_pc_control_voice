from fastapi import Request, Response
import logging

logger = logging.getLogger("api")

async def block_unwanted(request: Request, call_next):
    if request.url.path != "/alexapc" or request.method != "POST":
        logger.warning(f"Blocked request: {request.method} {request.url.path}")
        return Response(status_code=404)

    return await call_next(request)