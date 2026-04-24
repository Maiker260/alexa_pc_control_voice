import socket
import time

def wait_for_port(host, port):
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                return
        except OSError:
            time.sleep(0.2)