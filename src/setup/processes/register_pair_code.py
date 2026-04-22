import secrets
import time
import requests

from .generate_api_key import generate_api_key
from .generate_local_secret import generate_local_secret

def register_pair_code(domain):
    url = "https://nuizq83slj.execute-api.us-east-1.amazonaws.com/register"

    for _ in range(3):
        pair_code = str(secrets.randbelow(900000) + 100000)
        api_key = generate_api_key()
        secret_code = generate_local_secret()
        
        data = {
            "pair_code": pair_code,
            "device_secret": secret_code,
            "api_key": api_key,
            "domain": domain,
            "expires_at": int(time.time()) + 300
        }

        try:
            response = requests.post(url, json=data, timeout=5)

            if response.status_code == 200:
                return pair_code, api_key, secret_code

            if response.status_code == 409:
                continue

            raise Exception(f"Error API: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Register error: {e}")

    raise Exception("Unable to register the code after many attempts.")