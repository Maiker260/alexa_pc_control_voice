import json

def build_payload(action: str, data: dict):
    payload = {
        "action": action,
        **(data or {})
    }

    body = json.dumps(payload, separators=(",", ":"))

    return body