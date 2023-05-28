from django.db import models


class TeleSettings(models.Model):
    tb_token = models.CharField(max_length=200, verbose_name='Токен')
    tb_chat = models.CharField(max_length=200, verbose_name='Чат id')
    tb_message = models.TextField(verbose_name='Текст повідомлення')

    def __str__(self):
        return self.tb_message

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'
