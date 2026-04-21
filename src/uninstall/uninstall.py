from src.utils.remove_directory import remove_directory
from src.utils.remove_files import remove_files
from .processes.cloudflare.stop_cloudflared import stop_cloudflared
from .processes.cloudflare.delete_tunnel import delete_tunnel
from .processes.cloudflare.remove_user_config import remove_user_config
from .processes.cloudflare.uninstall_cloudflared_package import uninstall_cloudflared_package
from .processes.media_player.uninstall_media_tools import uninstall_media_tools
from .processes.cloudflare.dns_cleanup_popup import dns_cleanup_popup
from .processes.cloudflare.open_cloudflare_dns import open_cloudflare_dns
from src.utils.PATHS import CLOUDFLARED_DIR, USER_CONFIG_FILES_DIR
from src.utils.load_user_config import load_user_config
from src.utils.show_popup import show_popup

def uninstall():
    try:
        domain = load_user_config().get("domain")
    except RuntimeError:
        domain = None

    try:
        uninstall_media_tools()
        print("Media Player removed successfully")

        stop_cloudflared()
        delete_tunnel()
        remove_user_config()

        remove_directory(CLOUDFLARED_DIR, "CLOUDFLARED_DIR")
        remove_files(USER_CONFIG_FILES_DIR, ["app_config.json", "U2ck.txt"])

        uninstall_cloudflared_package()
        print("Cloudflared removed successfully")

        if domain:
            dns_cleanup_popup(domain)
            open_cloudflare_dns(domain)

        show_popup("Uninstall Complete", "All components were successfully removed.")

    except Exception as e:
        show_popup("Uninstall Error", str(e))
        raise