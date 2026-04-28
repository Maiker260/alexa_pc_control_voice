import socket
import time
import logging

def wait_for_port(host, port, timeout=10):
    logging.info(f"Checking FastAPI port {host}:{port}...")

    start = time.time()
    
    while True:
        try:
            with socket.create_connection((host, port), timeout=1):
                logging.info(f"Port {port} is open")
                return True

        except OSError:
            if time.time() - start > timeout:
                logging.error(f"Timeout: Port {port} did not open in {timeout}s")
                return False
            time.sleep(0.2)