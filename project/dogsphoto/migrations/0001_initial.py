# Generated by Django 4.2.7 on 2023-11-14 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogsPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_data', models.DateTimeField(default=datetime.datetime(2023, 11, 14, 20, 51, 11, 2095), null=True, verbose_name='Дата создания')),
                ('message', models.URLField(max_length=255, verbose_name='Ссылка на фото')),
                ('status', models.CharField(max_length=100, verbose_name='Статус ответа')),
            ],
        ),
    ]