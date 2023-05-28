from django.db import models


class PriceCard(models.Model):
    p_val = models.CharField(max_length=20, verbose_name='Ціна')
    p_description = models.CharField(max_length=200, verbose_name='Опис')

    def __str__(self):
        return self.p_val

    class Meta:
        verbose_name = 'Ціну'
        verbose_name_plural = 'Ціни'


class PriceTable(models.Model):
    p_title = models.CharField(max_length=200, verbose_name='Послуга')
    p_old = models.CharField(max_length=200, verbose_name='Стара ціна')
    p_new = models.CharField(max_length=200, verbose_name='Нова')

    def __str__(self):
        return self.p_title

    class Meta:
        verbose_name = 'Послугу'
        verbose_name_plural = 'Послуги'
