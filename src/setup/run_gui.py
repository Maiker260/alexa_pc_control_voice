from tkinter import *
from setup.gui.create_on_submit import create_on_submit
from setup.gui.create_start_setup import create_start_setup
from setup.gui.create_logger import create_logger

def run_gui(on_submit_callback):
    root = Tk()
    root.title("Alexa Setup")
    root.geometry("400x300")

    Label(root, text="Domain (ex: api.mydomain.com)").pack(pady=10)

    entry = Entry(root, width=40)
    entry.pack()

    status_label = Label(root, text="")
    status_label.pack(pady=5)

    log_box = Text(root, height=10, width=45)
    log_box.pack(pady=10)

    # LOGGER
    log = create_logger(root, status_label, log_box)

    # START SETUP
    start_setup = create_start_setup(root, on_submit_callback, log)

    # ON SUBMIT
    on_submit = create_on_submit(entry, status_label, log_box, start_setup)

    Button(root, text="Start Setup", command=on_submit).pack(pady=10)

    root.mainloop()