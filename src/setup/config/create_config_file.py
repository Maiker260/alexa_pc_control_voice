from .create_credentials_file import get_credentials_file
from src.utils.get_config_path import get_yaml_path

def create_config_file(domain):
    credentials_file = get_credentials_file()

    config = f"""
tunnel: alexa-tunnel
credentials-file: {credentials_file}

ingress:
  - hostname: {domain}
    service: http://127.0.0.1:8000
  - service: http_status:404
"""

    path = get_yaml_path()

    with open(path, "w") as f:
        f.write(config)

    return path