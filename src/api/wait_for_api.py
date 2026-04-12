import requests
import time

def wait_for_api():
    for _ in range(10):
        try:
            requests.get("http://127.0.0.1:8000/")
            return True
        except:
            time.sleep(1)
    return False