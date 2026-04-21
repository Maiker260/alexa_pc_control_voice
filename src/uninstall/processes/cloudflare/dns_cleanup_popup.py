from src.utils.show_popup import show_popup

def dns_cleanup_popup(domain):
    title = "Cleanup Notice"

    message = f"""
Cloudflare cleanup may be required.

1. A browser window will open.
2. Go to the DNS section.
3. Delete any existing record for:
   {domain}

This step may be required to fully uninstall the application.
"""
    
    show_popup(title, message)