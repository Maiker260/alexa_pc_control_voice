from fastapi import HTTPException
import time
import hmac
import hashlib
import logging

logger = logging.getLogger("api")

def validate_signature(headers, body: bytes, device_secret: str):
    timestamp = headers.get("x-timestamp")
    signature = headers.get("x-signature")

    if not timestamp or not signature:
        logger.warning("Missing security headers")
        raise HTTPException(status_code=400, detail="Missing headers")

    try:
        timestamp_int = int(timestamp)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid timestamp")

    if abs(time.time() - timestamp_int) > 30:
        logger.warning("Expired request")
        raise HTTPException(status_code=401, detail="Expired request")

    body_str = body.decode("utf-8")

    expected_signature = hmac.new(
        device_secret.encode(),
        (timestamp + body_str).encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        logger.warning("Invalid signature")
        raise HTTPException(status_code=403)