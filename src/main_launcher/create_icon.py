from pystray import Icon, Menu, MenuItem
from PIL import Image
from .on_exit import on_exit
from pathlib import Path

def create_icon():
    icon_path = Path(__file__).parent / "assets" / "icon.png"
    image = Image.open(icon_path)

    icon = Icon(
        "AlexaPC",
        image,
        "Alexa PC Control",
        menu=Menu(
            MenuItem("Exit", on_exit)
        )
    )

    icon.run()