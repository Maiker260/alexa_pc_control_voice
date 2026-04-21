import os
import time
import shutil

def remove_directory(path, name):
    if os.path.exists(path):
        time.sleep(2)
        shutil.rmtree(path)
        print(f"{name} deleted.")
    else:
        print(f"{name} not found, skipping.")