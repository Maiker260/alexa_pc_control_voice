from .cloudflare.login import login
from .cloudflare.create_tunnel import create_tunnel
from .cloudflare.route_dns import route_dns
from .cloudflare.install_cloudflared import install_cloudflared
from src.utils.is_installed import is_installed
from src.utils.tunnel_data import tunnel_name

def cloudflared_setup(write, domain, log):
    if not is_installed("cloudflared"):
        write("Installing Cloudflared Software...")
        install_cloudflared()

    write("Logging into Cloudflared...")
    write("A browser window will open. Please select your domain and authorize it to continue.", True)
    login()

    write("Creating Cloudflared Tunnel...")
    create_tunnel(tunnel_name)

    write("Creating DNS Entry...")
    route_dns(domain, log)

    write("Cloudflared setup done.")