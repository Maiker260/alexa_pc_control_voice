import requests

def post(url: str, body: str, headers: dict):
    response = requests.post(
        url,
        data=body,
        headers=headers,
        timeout=5
    )

    try:
        data = response.json()
    except Exception:
        data = {}

    return response.status_code, data, response.text