from src.utils.show_popup import show_popup

def notify_user_about_tunnel_wait():
    show_popup(
        "Uninstall in progress",
        "Active Cloudflare connections detected.\n\n"
        "We are waiting for the tunnel to fully disconnect.\n"
        "This may take up to a minute."
    )