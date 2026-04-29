import logging

from .processes.cloudflared_setup import cloudflared_setup
from .processes.media_player_setup import media_player_setup
from .config.create_config_file import create_config_file
from .config.save_app_config import save_app_config
from .processes.register_pair_code import register_pair_code
from src.utils.tunnel_data import tunnel_name
from src.utils.ensure_playlist_file import ensure_playlist_file

def run_setup(domain: str, log=None):
    def write(msg, require = None):
        prefix = "[REQUIRE]" if require else "[SETUP]"
        full_msg = f"{prefix} {msg}"

        if log:
            log(full_msg)

        logging.info(full_msg)

    try:
        write("Generating secure device credentials...")
        pair_code, api_key, secret_code = register_pair_code(domain)

        write("Installing Cloudflare Components...")
        cloudflared_setup(write, domain, log)

        write("Installing Media Player Components...")
        media_player_setup(write)

        write("Creating playlists template...")
        ensure_playlist_file()

        write("Creating config.yml...")
        create_config_file(domain)

        write("Saving Configuration...")
        save_app_config(domain, api_key, secret_code, tunnel_name)

        write("Setup Done.")
        write("You can close this window and continue with the installation")
    except Exception:
        logging.exception("Setup Error")
        write("Setup Error occurred. Check setup logs.")
        raise

    return pair_code