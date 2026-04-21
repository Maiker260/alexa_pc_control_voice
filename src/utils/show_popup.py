import ctypes

def show_popup(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)