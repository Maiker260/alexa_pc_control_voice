import urllib.request
import time

def wait_for_api():
    for _ in range(10):
        try:
            response = urllib.request.urlopen("http://127.0.0.1:8000/")
            if response.status == 200:
                return True
        except:
            time.sleep(1)
    return False