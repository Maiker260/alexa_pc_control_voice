from .processes.cloudflared_setup import cloudflared_setup
from .processes.media_player_setup import media_player_setup
from .config.create_config_file import create_config_file
from .config.save_app_config import save_app_config
from .processes.generate_api_key import generate_api_key
from src.utils.tunnel_data import tunnel_name

def run_setup(domain: str, log=None):
    def write(msg):
        prefix = "[SETUP]"
        if log:
            log(f"{prefix} {msg}")
        else:
            print(f"{prefix} {msg}")

    try:
        write("Generating API Key...")
        api_key = generate_api_key()

        write("Installing Cloudflare Components...")
        cloudflared_setup(write, domain, log)

        write("Installing Media Player Components...")
        media_player_setup(write)

        write("Creating config.yml...")
        create_config_file(domain)

        write("Saving Configuration...")
        save_app_config(domain, api_key, tunnel_name)

        write("Setup Done.")
    except Exception as e:
        write(f"Setup Error: {e}")
        raise