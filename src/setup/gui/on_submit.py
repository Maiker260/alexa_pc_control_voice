import threading
from tkinter import END

def create_on_submit(entry, status_label, log_box, start_setup):

    def on_submit():
        domain = entry.get().strip()

        if not domain:
            status_label.config(text="Enter your Domain")
            return

        log_box.delete("1.0", END)
        status_label.config(text="Starting setup...")

        threading.Thread(target=start_setup, args=(domain,), daemon=True).start()

    return on_submit