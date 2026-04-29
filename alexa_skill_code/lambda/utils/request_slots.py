def request_slots(handler_input):
    try:
        return handler_input.request_envelope.request.intent.slots or {}
    except Exception:
        return {}