from utils.user import get_user_id
from utils.persistence import get_user_data

def get_user_config(handler_input):
    user_id = get_user_id(handler_input)
    user_data = get_user_data(user_id)

    domain = user_data.get("domain")
    api_key = user_data.get("api_key")
    device_secret = user_data.get("device_secret")

    return api_key, device_secret, domain