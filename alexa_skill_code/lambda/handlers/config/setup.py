from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from utils.get_user_config import get_user_config
from utils.persistence import get_user_data, save_user_data
from utils.user import get_user_id

class SetupHandler(AbstractRequestHandler):
    "Handler to start the Setup"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SetupIntent")(handler_input)
        
    def handle(self, handler_input):
        return (
            handler_input.response_builder
                .speak("Para conectar tu computadora, dime el código que aparece en ella. Solo di: Mi codigo es, seguido del codigo.")
                .ask("¿Cuál es tu código?")
                .response
        )