from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from api.send_post_request import send_post_request
from utils.require_user_config import require_user_config
from utils.request_slots import request_slots
from utils.get_slot_value import get_slot_value

class OpenApplicationHandler(AbstractRequestHandler):
    "Handler to open an application in the PC"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("OpenApplicationIntent")(handler_input)

    @require_user_config
    def handle(self, handler_input):
        slots = request_slots(handler_input)
        app_name = get_slot_value(slots, "app_name")
        
        data = {
            "app_name": app_name
        }
        
        success, result = send_post_request(handler_input, "open_application", data)
        
        if not success:
            return (
                handler_input.response_builder
                    .speak("No puedo conectarme a tu computadora.")
                    .response
            )
        
        speak_output = f"Servido mi Rey, ya le abro el {app_name}."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )