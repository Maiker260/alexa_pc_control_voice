from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from api.send_post_request import send_post_request
from utils.require_user_config import require_user_config

class SkipMusicHandler(AbstractRequestHandler):
    "Handler to skip music"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("SkipMusicIntent")(handler_input)

    @require_user_config
    def handle(self, handler_input):

        data = {
            "music_action": "skip",
        }
        
        success, result = send_post_request(handler_input, "music", data)
        
        if not success:
            return (
                handler_input.response_builder
                    .speak("No puedo conectarme a tu computadora.")
                    .response
            )
        
        speak_output = f"Servido mi Rey, ya le pongo la siguiente cancion en la lista."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )