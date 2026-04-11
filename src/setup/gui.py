import threading
from tkinter import *

def run_gui(on_submit_callback):
    
    def start_setup(domain):
        try:
            on_submit_callback(domain)
            root.after(0, lambda: status_label.config(text="Setup Done"))
        except Exception as e:
            root.after(0, lambda: status_label.config(text=f"Error: {e}"))

    def on_submit():
        domain = entry.get()
        
        if not domain:
            status_label.config(text="Enter your Domain")
            return

        status_label.config(text="Starting setup...")

        threading.Thread(target=start_setup, args=(domain,)).start()

    root = Tk()
    root.title("Alexa Setup")
    root.geometry("350x200")

    Label(root, text="Domain (ex: api.mydomain.com)").pack(pady=10)

    entry = Entry(root, width=30)
    entry.pack()

    Button(root, text="Start Setup", command=on_submit).pack(pady=10)

    status_label = Label(root, text="")
    status_label.pack(pady=10)

    root.mainloop()