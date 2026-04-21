import webbrowser

def open_cloudflare_dns(domain):
    url = f"https://dash.cloudflare.com/?to=/:account/{domain}/dns"

    webbrowser.open(url)