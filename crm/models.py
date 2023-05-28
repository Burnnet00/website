from django.db import models

class StatusCrm(models.Model):
    status = models.CharField(max_length=200, verbose_name='Сатус')

    def __str__(self):
        return self.status


    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'

class Orders(models.Model):
    o_date = models.DateTimeField(auto_now=True)
    o_name = models.CharField(max_length=200, verbose_name='Імя')
    o_phone = models.CharField(max_length=200, verbose_name='Телефон')
    o_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    def __str__(self):
        return self.o_name

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

class ComentCrm(models.Model):
    coment = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заявка')
    coment_text = models.TextField(verbose_name='Текст коменту')
    coment_db = models.DateTimeField(auto_now=True, verbose_name='Дата створення')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Коментарій'
        verbose_name_plural = 'Коментарії'


