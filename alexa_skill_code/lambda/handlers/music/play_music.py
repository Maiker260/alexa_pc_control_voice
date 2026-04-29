from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from api.send_post_request import send_post_request
from utils.require_user_config import require_user_config

class PlayMusicHandler(AbstractRequestHandler):
    "Handler to play music"
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("PlayMusicIntent")(handler_input)

    @require_user_config
    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        song_name = slots["song_name"].value if slots.get("song_name") else ""

        data = {
            "music_action": "play",
            "song_name": song_name
        }
        
        success, result = send_post_request(handler_input, "music", data)
        
        if not success:
            return (
                handler_input.response_builder
                    .speak("No puedo conectarme a tu computadora.")
                    .response
            )
        
        speak_output = f"Servido mi Rey, ya le pongo la pieza de {song_name}."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )