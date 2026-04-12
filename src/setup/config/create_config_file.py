import os
from src.utils.PATHS import USER_DATA_DIR

def create_config_file(domain):
    config = f"""
tunnel: alexa-tunnel
credentials-file: C:\\Users\\%USERNAME%\\.cloudflared\\*.json

ingress:
  - hostname: {domain}
    service: http://localhost:8000
  - service: http_status:404
"""
    path = os.path.join(USER_DATA_DIR, "config.yml")

    with open(path, "w") as f:
        f.write(config)

    return path