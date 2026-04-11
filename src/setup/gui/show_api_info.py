from tkinter import Toplevel, Label, Button
from src.utils.load_user_config import load_user_config
from src.setup.config.get_config_path import get_config_path
from .copy_key import copy_key

def show_api_info(domain):
    config = load_user_config()
    API_KEY = config["api_key"]
    api_path = get_config_path()

    win = Toplevel()
    win.title("Setup Completed")
    win.geometry("400x250")

    Label(win, text="Setup Completed!", font=("Arial", 12, "bold")).pack(pady=10)

    Label(
        win,
        text=f"Your domain is:\n{domain}",
        wraplength=350,
        justify="center"
    ).pack(pady=5)

    Label(
        win,
        text=(
            "Setup Completed!\n\n"
            "Your API Key:\n"
            f"{API_KEY}\n\n"
            "Saved at:\n"
            f"{api_path}\n\n"
            "Next step:\n"
            "Add this API Key to your Alexa App configuration."
        ),
        wraplength=350,
        justify="left"
    ).pack(pady=10)

    Button(win, text="Copy API Key", command=lambda: copy_key(Label, win, API_KEY)).pack(pady=5)
    Button(win, text="Close", command=win.destroy).pack(pady=10)