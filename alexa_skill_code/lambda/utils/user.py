def get_user_id(handler_input):
    return handler_input.request_envelope.context.system.user.user_id