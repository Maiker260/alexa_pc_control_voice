import secrets
import time
import requests

from .generate_api_key import generate_api_key
from .generate_local_secret import generate_local_secret

def register_pair_code(domain):
    pair_code = str(secrets.randbelow(900000) + 100000) # 6 Digits
    api_key = generate_api_key()
    secret_code = generate_local_secret()

    data = {
        "pair_code": pair_code,
        "device_secret": secret_code,
        "api_key": api_key,
        "domain": domain,
        "expires_at": int(time.time()) + 300 # 5min
    }

    requests.post(
        "https://nuizq83slj.execute-api.us-east-1.amazonaws.com/register",
        json=data,
    )

    return pair_code, api_key, secret_code