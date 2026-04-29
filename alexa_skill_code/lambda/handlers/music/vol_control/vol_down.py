from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from api.send_post_request import send_post_request
from utils.require_user_config import require_user_config

class VolDownHandler(AbstractRequestHandler):
    "Handler to control the volume down"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("VolDownIntent")(handler_input)

    @require_user_config
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        vol_value = slots["vol_value"].value if slots.get("vol_value") else ""

        data = {
            "music_action": "volume",
            "vol_action": "vol_down",
            "vol_value": vol_value,
        }

        success, result = send_post_request(handler_input, "music", data)

        if not success:
            return (
                handler_input.response_builder
                    .speak("No puedo conectarme a tu computadora.")
                    .response
            )

        speak_output = f"Servido mi Rey, ya le bajo el volumen."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )