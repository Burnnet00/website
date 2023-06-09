import requests
from .models import TeleSettings


def sendTelegram(tb_name, tb_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tb_token)
        chat_id = str(settings.tb_chat)
        text = str(settings.tb_message)
        api = "https://api.telegram.org/bot"
        method = api + token + "/sendMessage"

        # Зателефонуйте:
        # Імя: {name}
        # Телефон: {phone}

        # a = text.find('{')  # шукаємо текстові зміні імені що в дужках
        # b = text.find('}')
        # c = text.rfind('{')  # змінна телефону витягуємо наступною
        # d = text.rfind('}')  # через новий метод
        #
        # part_1 = text[0:a]  # від ноля до дужки
        # part_2 = text[b + 1:c]  # вирізаємо +1(без дужки)
        # part_3 = text[d:-1]  # вирізаємо від д до oстаннього символу

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('{'):

            part_1 = text[0:text.find('{')]  # від ноля до дужки
            part_2 = text[text.find('}') + 1:text.rfind('{')]  # вирізаємо +1(без дужки)
            part_3 = text[text.rfind('}'):-1]  # вирізаємо від д до oстаннього символу

            text_slise = part_1 + tb_name + part_2 + tb_phone + part_3  # три часті тексту з адмінки додаються до змінних імя та тел з пост запиту

        else:
            text_slise = text
        # Зателефонуйте:
        # Імя:
        # Телефон:
        # Тепер прописуємо вхідні дані в функцію: (tb_name, tb_phone) та text_slise
        try:
            reg = requests.post(method, data={
                "chat_id": chat_id,
                "text": text_slise
            })  # фіункція відправки запиту (reg = server)
        except:
            pass
        finally:
            if reg.status_code != 200:
                print('Помилка відправки')
            elif reg.status_code == 500:
                print('Помилка 500')
            else:
                print('Повідомлення відправлене')

    else:

        pass
