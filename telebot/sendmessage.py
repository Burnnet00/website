import requests
from .models import TeleSettings


def sendTelegram(tb_name, tb_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tb_token)
    chat_id = str(settings.tb_chat)
    text = str(settings.tb_message)
    api = "https://api.telegram.org/bot"
    method = api + token + "/sendMessage"

    # Зателефонуйте:
    # Імя: {name}
    # Телефон: {phone}

    a = text.find('{')  # шукаємо текстові зміні імені що в дужках
    b = text.find('}')
    c = text.rfind('{')  # змінна телефону витягуємо наступною
    d = text.rfind('}')  # через новий метод

    part_1 = text[0:a]  # від ноля до дужки
    part_2 = text[b + 1:c]  # вирізаємо +1(без дужки)
    part_3 = text[d:-1]  # вирізаємо від д до oстаннього символу

    text_slise = part_1 + tb_name + part_2 + tb_phone + part_3# три часті тексту з адмінки додаються до змінних імя та тел з пост запиту

    # Зателефонуйте:
    # Імя:
    # Телефон:
    # Тепер прописуємо вхідні дані в функцію: (tb_name, tb_phone) та text_slise

    reg = requests.post(method, data={
        "chat_id": chat_id,
        "text": text_slise
    })
