# Generated by Django 4.2.1 on 2023-05-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cmsslider',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайди'},
        ),
        migrations.AddField(
            model_name='cmsslider',
            name='c_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='Kaс'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='c_img',
            field=models.ImageField(upload_to='sliderimg/', verbose_name='Загрузити'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='c_text',
            field=models.CharField(max_length=200, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='c_title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
