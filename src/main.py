import logging
from fastapi import FastAPI, Request, HTTPException

from src.middleware.block_unwanted import block_unwanted
from src.utils.get_keys import get_keys
from src.security.auth import validate_auth
from src.security.signature import validate_signature
from src.handlers.handle_request import handle_request

app = FastAPI()
logger = logging.getLogger("api")

app.middleware("http")(block_unwanted)

@app.post("/alexapc")
async def alexa(request: Request):    
    API_KEY, DEVICE_SECRET = get_keys()

    validate_auth(request.headers, API_KEY, DEVICE_SECRET)

    body = await request.body()
    validate_signature(request.headers, body, DEVICE_SECRET)

    try:
        data = await request.json()
    except Exception:
        logger.warning("Invalid JSON received")
        raise HTTPException(status_code=400, detail="Invalid JSON")

    try:
        logging.info("Processing Alexa request")
        result = handle_request(data)
        logging.info("Request processed successfully")

        return {
            "success": True,
            "result": result
        }

    except Exception:
        logging.exception("Error processing request")

        return {
            "success": False,
            "error": "Internal server error"
        }