import browser_cookie3
from pathlib import Path
from .PATHS import USER_CONFIG_FILES_DIR

def get_firefox_cookies():
    cj = browser_cookie3.firefox(domain_name='.youtube.com')
    print("Cookie")
    config_dir = Path(USER_CONFIG_FILES_DIR)
    config_dir.mkdir(parents=True, exist_ok=True)

    cookies_path = config_dir / "U2ck.txt"

    with open(cookies_path, "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")

        for c in cj:
            domain = c.domain

            if not domain.startswith("."):
                domain = "." + domain

            expires = int(c.expires) if c.expires else 0
            if expires > 1e12:
                expires = int(expires / 1000)

            f.write(
                f"{domain}\t"
                f"TRUE\t"
                f"{c.path}\t"
                f"{'TRUE' if c.secure else 'FALSE'}\t"
                f"{expires}\t"
                f"{c.name}\t"
                f"{c.value}\n"
            )