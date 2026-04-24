import sys
import os

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)

    return os.path.join(os.path.dirname(__file__), filename)