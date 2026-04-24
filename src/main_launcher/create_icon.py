from pystray import Icon, Menu, MenuItem
from PIL import Image
from .on_exit import on_exit
from src.utils.get_asset_path import get_asset_path

def create_icon():
    image = Image.open(get_asset_path("icon.ico"))

    icon = Icon(
        "AlexaPC",
        image,
        "Alexa PC Voice Control",
        menu=Menu(
            MenuItem("Alexa PC Voice Control", None, enabled=False, default=False),
            MenuItem("Exit", on_exit)
        )
    )

    icon.run()