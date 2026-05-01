from utils.get_user_config import get_user_config
from utils.is_valid_domain import is_valid_domain

from api.payload import build_payload
from api.signer import generate_signature
from api.http import post

def send_post_request(handler_input, action, data=None):
    api_key, device_secret, domain = get_user_config(handler_input)

    if not is_valid_domain(domain):
        return False, "Invalid domain"

    url = f"https://{domain}/alexapc"

    try:
        body = build_payload(action, data)

        timestamp, signature = generate_signature(device_secret, body)

        headers = {
            "x-api-key": api_key,
            "x-device-secret": device_secret,
            "x-timestamp": timestamp,
            "x-signature": signature,
            "Content-Type": "application/json"
        }

        status_code, response_data, raw = post(url, body, headers)

        if status_code != 200:
            raise Exception(f"HTTP error: {status_code}")

        if not response_data.get("success"):
            raise Exception(response_data.get("error", "Unknown API error"))
            
        return True, response_data

    except Exception as e:
        print(f"PC API Error: {e}")
        return False, str(e)