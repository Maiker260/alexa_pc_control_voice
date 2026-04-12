from tkinter import END

def create_logger(root, status_label, log_box):

    def log_to_ui(message):
        def update():
            status_label.config(text=message)
            log_box.insert(END, message + "\n")
            log_box.see(END)

        root.after(0, update)

    return log_to_ui