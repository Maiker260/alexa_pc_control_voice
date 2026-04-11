from .processes.login import login
from .processes.create_tunnel import create_tunnel
from .processes.route_dns import route_dns
from .config.create_config_file import create_config_file
from .config.save_app_config import save_app_config
from .processes.install_cloudflared import install_cloudflared
from .processes.is_cloudflared_installed import is_cloudflared_installed
from .processes.generate_api_key import generate_api_key
from src.utils.tunnel_data import tunnel_name

def run_setup(domain: str):
    print("=== Setup Alexa Automation ===")

    api_key = generate_api_key()

    if not is_cloudflared_installed():
        install_cloudflared()

    login()
    create_tunnel(tunnel_name)
    route_dns(domain)

    create_config_file(domain)
    save_app_config(domain, api_key, tunnel_name)

    print("\n=== CONFIGURACIÓN ===")
    print(f"URL: https://{domain}/alexa")
    print(f"API KEY: {api_key}")