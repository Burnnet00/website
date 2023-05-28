from django.db import models

class CmsSlider(models.Model):
    c_img = models.ImageField(upload_to='sliderimg/', verbose_name='Загрузити')
    c_title = models.CharField(max_length=200, verbose_name='Заголовок')
    c_text = models.CharField(max_length=200, verbose_name='Текст')
    c_css = models.CharField(max_length=200, null=True, default='-', verbose_name='Kaс')

    def __str__(self):
        return self.c_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайди'

