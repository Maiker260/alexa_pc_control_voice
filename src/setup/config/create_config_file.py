def create_config_file(domain):
    config = f"""
tunnel: alexa-tunnel
credentials-file: C:\\Users\\%USERNAME%\\.cloudflared\\*.json

ingress:
  - hostname: {domain}
    service: http://localhost:8000
  - service: http_status:404
"""
    with open("config.yml", "w") as f:
        f.write(config)