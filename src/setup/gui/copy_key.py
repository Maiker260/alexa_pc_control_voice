def copy_key(Label ,win, API_KEY):
    win.clipboard_clear()
    win.clipboard_append(API_KEY)
    Label(win, text="Copied!", fg="green").pack()