import sys
import psutil
import logging

import src.main_launcher.process_manager as pm

def kill_process_tree(pid):
    try:
        parent = psutil.Process(pid)
        
        for child in parent.children(recursive=True):
            child.kill()

        parent.kill()

    except Exception:
        logging.exception("Kill error")

def on_exit(icon, item):
    logging.info("Shutting down...")

    if pm.process:
        logging.info("Killing cloudflared PID: %s", pm.process.pid)
        kill_process_tree(pm.process.pid)

    icon.stop()
    sys.exit(0)