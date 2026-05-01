import logging

from src.utils.remove_directory import remove_directory
from src.utils.remove_files import remove_files
from .processes.cloudflare.delete_tunnel import delete_tunnel
from .processes.cloudflare.remove_user_config import remove_user_config
from .processes.cloudflare.uninstall_cloudflared_package import uninstall_cloudflared_package
from .processes.media_player.uninstall_media_tools import uninstall_media_tools
from .processes.cloudflare.dns_cleanup_popup import dns_cleanup_popup
from .processes.cloudflare.open_cloudflare_dns import open_cloudflare_dns
from src.utils.PATHS import CLOUDFLARED_DIR, USER_CONFIG_FILES_DIR
from src.utils.load_user_config import load_user_config
from src.utils.setup_logging import setup_logging
from .processes.cloudflare.stop_processes import stop_processes
from .processes.cloudflare.wait_for_tunnel_close import wait_for_tunnel_close
from .processes.cloudflare.notify_user_about_tunnel_wait import notify_user_about_tunnel_wait
from src.utils.tunnel_data import tunnel_name

def cleanup_task(name, func):
    try:
        logging.info(f"Starting: {name}")
        func()
        logging.info(f"Completed: {name}")
        return True

    except Exception:
        logging.exception(f"Failed: {name}")
        return False

def uninstall():
    setup_logging("uninstall.log")
    logging.info("Starting uninstall cleanup...")

    try:
        domain = load_user_config().get("domain")
    except Exception:
        logging.warning("No user config found")
        domain = None

    tasks = [
        ("Stopping Services", stop_processes),
        ("Uninstall media tools", uninstall_media_tools),
    ]

    for name, func in tasks:
        cleanup_task(name, func)

    if not wait_for_tunnel_close(tunnel_name, check_only=True):
        notify_user_about_tunnel_wait()

    if wait_for_tunnel_close(tunnel_name):
        logging.info("Tunnel is safe to delete now.")
    else:
        logging.warning("Proceeding with tunnel delete anyway (timeout).")

    cleanup_task("Deleting tunnel", delete_tunnel)

    more_tasks = [
        ("Removing user config", remove_user_config),
        ("Removing directories", lambda: remove_directory(CLOUDFLARED_DIR, "CLOUDFLARED_DIR")),
        ("Removing files", lambda: remove_files(USER_CONFIG_FILES_DIR, ["app_config.json", "U2ck.txt"])),
        ("Uninstalling cloudflared package", uninstall_cloudflared_package),
    ]

    for name, func in more_tasks:
        cleanup_task(name, func)

    if domain:
        logging.info(f"Cleaning DNS for domain: {domain}")
        cleanup_task("DNS cleanup popup", lambda: dns_cleanup_popup(domain))
        cleanup_task("Open Cloudflare DNS", lambda: open_cloudflare_dns(domain))

    logging.info("Uninstall completed successfully")