import requests

token = "6065387831:AAFgmhoD6Ank5TPs2-TbNPPtbOLb0iGyjcw"#"826321393:AAGOrh6yQ2y8MjsZDNR7539VAHroTUdVQ9s"
chat_id = "-991007410"
text = "Test_2"

#https://api.telegram.org/bot

def SendTelegram():
    api = "https://api.telegram.org/bot"
    method = api + token + "/sendMessage"
    reg = requests.post(method, data={
        "chat_id": chat_id,
        "text": text
    })

SendTelegram()