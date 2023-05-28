import requests
from .models import TeleSettings



def sendTelegram():
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tb_token)
    chat_id = str(settings.tb_chat)
    text = str(settings.tb_message)
    api = "https://api.telegram.org/bot"
    method = api + token + "/sendMessage"


    reg = requests.post(method, data={
        "chat_id": chat_id,
        "text": text
    })



