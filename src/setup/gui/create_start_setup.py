from src.utils.show_popup import show_popup
def create_start_setup(root, on_submit_callback, log):

    def start_setup(domain):
        message = (
            "Setup completed successfully!\n\n"
            "Next steps:\n"
            "1. Enable the Alexa skill: 'Alexa, vamoa jugar'\n"
            f"2. Configure your domain: 'Configura mi dominio {domain}'\n"
            "3. Add your device: 'Agrega mi nuevo dispositivo 12345'\n"
        )

        title = "Setup Complete"

        try:
            on_submit_callback(domain, log=log)
            root.after(0, lambda: show_popup(message, title))
        except Exception as e:
            log(f"Error: {e}")

    return start_setup