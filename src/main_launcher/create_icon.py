from pystray import Icon, Menu, MenuItem
from PIL import Image
from .on_exit import on_exit
from src.utils.get_asset_path import get_asset_path

def create_icon():
    image = Image.open(get_asset_path("assets/icon.png"))

    icon = Icon(
        "AlexaPC",
        image,
        "Alexa PC Control",
        menu=Menu(
            MenuItem("Exit", on_exit)
        )
    )

    icon.run()