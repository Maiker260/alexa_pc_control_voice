import os
import psutil
import src.main_launcher.process_manager as pm

def kill_process_tree(pid):
    try:
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
    except Exception as e:
        print("Kill error:", e)

def on_exit(icon, item):
    print("Shutting down...")

    if pm.process:
        print("Killing cloudflared PID:", pm.process.pid)
        kill_process_tree(pm.process.pid)

    icon.stop()
    os._exit(0)