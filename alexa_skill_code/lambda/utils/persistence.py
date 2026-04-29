import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("DYNAMODB_PERSISTENCE_TABLE_NAME"))


def get_user_data(user_id):
    try:
        response = table.get_item(Key={"id": user_id})
        return response.get("Item", {})
    except Exception:
        return {}


def save_user_data(user_id, new_data):
    existing_data = get_user_data(user_id)

    updated_data = {
        "id": user_id,
        **existing_data,
        **new_data
    }

    table.put_item(Item=updated_data)