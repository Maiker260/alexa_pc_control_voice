import os
from src.utils.get_config_path import get_app_dir

def create_config_file(domain):
    config = f"""
tunnel: alexa-tunnel
credentials-file: C:\\Users\\%USERNAME%\\.cloudflared\\*.json

ingress:
  - hostname: {domain}
    service: http://localhost:8000
  - service: http_status:404
"""
    path = os.path.join(get_app_dir(), "config.yml")

    with open(path, "w") as f:
        f.write(config)

    return path