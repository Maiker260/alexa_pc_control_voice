import requests

from utils.get_user_config import get_user_config
from utils.is_valid_domain import is_valid_domain

def send_post_request(handler_input, action, data = None):
    api_key, device_secret, domain = get_user_config(handler_input)

    if not is_valid_domain(domain):
        return False, "Invalid domain"
    
    url = f"https://{domain}/alexapc"
        
    try:
        headers = {
            "x-api-key": api_key,
            "x-device-secret": device_secret
        }

        payload = {
            "action": action,
            **data
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except Exception:
            data = {}

        if response.status_code != 200:
            raise Exception(f"HTTP error: {response.status_code}")

        if not data.get("success"):
            raise Exception(data.get("error", "Unknown API error"))

        return True, data

    except Exception as e:
        print(f"PC API Error: {e}")
        
        return False, str(e)