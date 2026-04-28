import logging
from fastapi import FastAPI, Request, Response, HTTPException

from src.utils.get_keys import get_keys
from src.handlers.handle_request import handle_request

app = FastAPI()

logger = logging.getLogger("api")

@app.middleware("http")
async def block_unwanted(request: Request, call_next):
    if request.url.path != "/alexapc" or request.method != "POST":
        logging.warning(f"Blocked request: {request.method} {request.url.path}")
        return Response(status_code=404)

    return await call_next(request)

@app.post("/alexapc")
async def alexa(request: Request):    
    API_KEY, DEVICE_SECRET = get_keys()

    if request.headers.get("x-api-key") != API_KEY:
        logging.warning("Invalid API KEY attempt")
        raise HTTPException(status_code=401)

    if request.headers.get("x-device-secret") != DEVICE_SECRET:
        logging.warning("Invalid DEVICE SECRET attempt")
        raise HTTPException(status_code=403)

    try:
        data = await request.json()
    except Exception:
        logging.warning("Invalid JSON received")
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