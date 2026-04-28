import logging

from src.utils.show_popup import show_popup

def create_start_setup(root, on_submit_callback, log):

    def start_setup(domain):
        try:
            logging.info("Starting setup process...")
            
            pair_code = on_submit_callback(domain, log=log)

            logging.info("Setup completed successfully")
            
            title = "Setup Complete"
            message = (
                "Setup completed successfully!\n\n"
                "Next steps:\n\n"
                "1. Enable the Alexa skill. Say: 'Alexa, escritorio remoto'\n"
                "2. Say: 'Iniciar configuración'\n"
                f"3. Say: 'Mi código es {pair_code}'\n"
            )

            root.after(0, lambda: show_popup(title, message))

        except Exception as e:
            logging.exception("Setup failed")

            if log:
                log("Setup failed. Check setup logs for details.")

    return start_setup