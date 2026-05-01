import time
import hmac
import hashlib

def generate_signature(device_secret: str, body: str):
    timestamp = str(int(time.time()))

    message = timestamp + body

    signature = hmac.new(
        device_secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return timestamp, signature