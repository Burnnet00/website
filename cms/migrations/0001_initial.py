# Generated by Django 4.2.1 on 2023-05-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_img', models.ImageField(upload_to='sliderimg/')),
                ('c_title', models.CharField(max_length=200)),
                ('c_text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
    ]
