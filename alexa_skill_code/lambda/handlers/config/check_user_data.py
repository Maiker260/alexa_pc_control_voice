from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from utils.get_user_config import get_user_config

class CheckUserDataHandler(AbstractRequestHandler):
    "Handler to check user Data"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("CheckUserDataIntent")(handler_input)

    def handle(self, handler_input):
        api_key, domain = get_user_config(handler_input)
        
        speak_output = f"Dominio: {domain} y la clave es {api_key}"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )