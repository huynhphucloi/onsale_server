import firebase_admin
from firebase_admin import credentials, messaging
from pathlib import Path
import datetime

BASE_DIR = Path(__file__).resolve().parent

cred = credentials.Certificate(f'{BASE_DIR}/configs/auth_code.json')
firebase_admin.initialize_app(cred)


def updateShop(password):
    message = messaging.Message(
        data={"pass": f"{password}", "action": "update"},
        topic="doronUpdate"
    )
    response = messaging.send(message)
    print("Response Firebase: ", response)


def removeShop(password):
    message = messaging.Message(
        data={"pass": f"{password}", "action": 'remove'},
        topic="doronUpdate"
    )
    response = messaging.send(message)
    print("Response Firebase: ", response)


def sendNotification(instance):
    message = messaging.Message(
        notification=messaging.Notification(
            title=instance.title,
            body=instance.message,
            image=instance.image,
        ),
        topic=instance.topic
    )
    response = messaging.send(message)
    print("Response Firebase: ", response)