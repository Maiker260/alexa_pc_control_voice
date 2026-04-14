import os
from pathlib import Path

def find_app(name):
    if not name:
        raise ValueError("App name is required")

    name = name.lower()

    routes = [
        Path(os.getenv("APPDATA")) / r"Microsoft\Windows\Start Menu\Programs",
        Path(os.getenv("PROGRAMDATA")) / r"Microsoft\Windows\Start Menu\Programs"
    ]

    for route in routes:
        for file in route.rglob("*.lnk"):
            if file.stem.lower() == name:
                return file

    return None