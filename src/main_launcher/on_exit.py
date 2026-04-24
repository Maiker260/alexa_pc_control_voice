import os

def on_exit(icon, item):
    global process
    
    if process:
        process.terminate()
    
    icon.stop()
    os._exit(0)