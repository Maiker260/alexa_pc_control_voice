import ctypes

def show_popup(title, message):
    MB_ICONINFORMATION = 0x40
    ctypes.windll.user32.MessageBoxW(0, message, title, MB_ICONINFORMATION)