from src.utils.ensure_admin import ensure_admin
from src.utils.remove_directory import remove_directory
from src.utils.remove_files import remove_files
from .processes.cloudflare.stop_cloudflared import stop_cloudflared
from .processes.cloudflare.delete_tunnel import delete_tunnel
from .processes.cloudflare.remove_user_config import remove_user_config
from .processes.cloudflare.uninstall_cloudflared_package import uninstall_cloudflared_package
from .processes.media_player.uninstall_media_tools import uninstall_media_tools
from src.utils.PATHS import CLOUDFLARED_DIR, USER_CONFIG_FILES_DIR

def uninstall():
    uninstall_media_tools()
    print("Media Player removed successfully")

    ensure_admin()

    stop_cloudflared()
    delete_tunnel()
    remove_user_config()

    remove_directory(CLOUDFLARED_DIR, "CLOUDFLARED_DIR")
    remove_files(USER_CONFIG_FILES_DIR, ["app_config.json", "U2ck.txt"])

    uninstall_cloudflared_package()
    print("Cloudflared removed successfully")