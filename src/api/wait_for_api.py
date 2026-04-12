import requests
import time

def wait_for_api():
    for i in range(20):
        try:
            print(f"Checking API... ({i})")
            response = requests.get("http://127.0.0.1:8000/")
            print("Response:", response.status_code)

            if response.status_code == 200:
                return True
        except Exception as e:
            print("Error:", e)
            time.sleep(1)
            
    return False