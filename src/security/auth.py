from fastapi import HTTPException
import logging

logger = logging.getLogger("api")

def validate_auth(headers, api_key, device_secret):
    if headers.get("x-api-key") != api_key:
        logger.warning("Invalid API KEY attempt")
        raise HTTPException(status_code=401)

    if headers.get("x-device-secret") != device_secret:
        logger.warning("Invalid DEVICE SECRET attempt")
        raise HTTPException(status_code=403)