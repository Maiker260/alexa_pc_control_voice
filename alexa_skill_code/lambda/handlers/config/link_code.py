import requests
from ask_sdk_core.dispatch_components import AbstractRequestHandler
import ask_sdk_core.utils as ask_utils

from utils.persistence import save_user_data
from utils.user import get_user_id

API_URL = "https://nuizq83slj.execute-api.us-east-1.amazonaws.com/validate-code"


class LinkCodeHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LinkCodeIntent")(handler_input)

    def handle(self, handler_input):
        user_id = get_user_id(handler_input)
        code = handler_input.request_envelope.request.intent.slots["link_code"].value

        if not code:
            return (
                handler_input.response_builder
                    .speak("No entendí el código. Intenta de nuevo.")
                    .ask("¿Cuál es tu código?")
                    .response
            )

        try:
            response = requests.post(
                API_URL,
                json={"pair_code": code},
                timeout=5
            )

            data = response.json()

        except Exception:
            return (
                handler_input.response_builder
                    .speak("No pude conectar con el servidor.")
                    .response
            )

        if not data.get("success"):
            return (
                handler_input.response_builder
                    .speak("Ese código no es válido o ya expiró.")
                    .response
            )

        save_user_data(user_id, {
            "domain": data["domain"],
            "api_key": data["api_key"],
            "device_secret": data.get("device_secret")
        })

        return (
            handler_input.response_builder
                .speak("Listo. Computadora conectada.")
                .response
        )