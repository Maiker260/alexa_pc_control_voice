from src.setup.gui.show_api_info import show_api_info
def create_start_setup(root, on_submit_callback, log):

    def start_setup(domain):
        try:
            on_submit_callback(domain, log=log)
            root.after(0, lambda: show_api_info(domain))
        except Exception as e:
            log(f"Error: {e}")

    return start_setup