from django.db import models

class Orders(models.Model):
    o_date = models.DateTimeField(auto_now=True)
    o_name = models.CharField(max_length=200, verbose_name='Імя')
    o_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return self.o_name

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
