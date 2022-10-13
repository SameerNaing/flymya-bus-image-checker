import os
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery


SCOPES = [
    'https://www.googleapis.com/auth/chat.bot'
]


def __credential():
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
        "google-service-key.json", SCOPES)

    return discovery.build("chat", "v1", http=CREDENTIALS.authorize(Http()))


def send_message(message):
    SPACE_ID = os.getenv("CHAT_SPACE")
    try:
        __credential().spaces().messages().create(
            parent=f"spaces/{SPACE_ID}",
            body={"text": message}
        ).execute()

    except Exception as e:
        print(e)
        return
