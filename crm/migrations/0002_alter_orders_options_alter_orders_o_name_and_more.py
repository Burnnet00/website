# Generated by Django 4.2.1 on 2023-05-26 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='o_name',
            field=models.CharField(max_length=200, verbose_name='Імя'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='o_phone',
            field=models.CharField(max_length=200, verbose_name='Телефон'),
        ),
    ]
