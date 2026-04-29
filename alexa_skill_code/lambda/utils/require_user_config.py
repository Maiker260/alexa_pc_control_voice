from utils.persistence import save_user_data, get_user_data
from utils.user import get_user_id

def require_user_config(func):
    def wrapper(self, handler_input):
        user_id = get_user_id(handler_input)
        user_data = get_user_data(user_id)

        api_key = user_data.get("api_key")
        domain = user_data.get("domain")

        if not domain or not api_key:
            user_data["pending_setup"] = "domain" if not domain else "api_key"
            save_user_data(user_id, user_data)

            return (
                handler_input.response_builder
                    .speak("Te falta configuración. Reinstala la aplicacion en tu PC y dime el codigo para vincularme.")
                    .response
            )

        return func(self, handler_input)

    return wrapper