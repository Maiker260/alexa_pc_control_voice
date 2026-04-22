from .processes.cloudflared_setup import cloudflared_setup
from .processes.media_player_setup import media_player_setup
from .config.create_config_file import create_config_file
from .config.save_app_config import save_app_config
from .processes.register_pair_code import register_pair_code
from src.utils.tunnel_data import tunnel_name

def run_setup(domain: str, log=None):
    def write(msg, require = None):
        prefix = "[REQUIRE]" if require else "[SETUP]"

        if log:
            log(f"{prefix} {msg}")
        else:
            print(f"{prefix} {msg}")

    try:
        write("Generating API Key...")
        pair_code, api_key, secret_code = register_pair_code(domain)

        write("Installing Cloudflare Components...")
        cloudflared_setup(write, domain, log)

        write("Installing Media Player Components...")
        media_player_setup(write)

        write("Creating config.yml...")
        create_config_file(domain)

        write("Saving Configuration...")
        save_app_config(domain, api_key, secret_code, tunnel_name)

        write("Setup Done.")
        write("You can close this window and run the App Launcher.")
    except Exception as e:
        write(f"Setup Error: {e}")
        raise

    return pair_code