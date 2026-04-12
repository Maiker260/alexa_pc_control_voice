from .processes.login import login
from .processes.create_tunnel import create_tunnel
from .processes.route_dns import route_dns
from .config.create_config_file import create_config_file
from .config.save_app_config import save_app_config
from .processes.install_cloudflared import install_cloudflared
from .processes.is_cloudflared_installed import is_cloudflared_installed
from .processes.generate_api_key import generate_api_key
from src.utils.tunnel_data import tunnel_name

def run_setup(domain: str, log=None):
    def write(msg):
        if log:
            log(msg)
        else:
            print(msg)

    try:
        write("🔑 Generating API Key...")
        api_key = generate_api_key()

        if not is_cloudflared_installed():
            write("Installing Cloudflared...")
            install_cloudflared()

        write("Logging into Cloudflared...")
        login()

        write("Creating Cloudflared Tunnel...")
        create_tunnel(tunnel_name)

        write("Creating DNS Entry...")
        route_dns(domain, log)

        write("Creating config.yml...")
        create_config_file(domain)

        write("Saving Configuration...")
        save_app_config(domain, api_key, tunnel_name)

        write("Setup Done.")
    except Exception as e:
        write(f"Setup Error: {e}")
        raise