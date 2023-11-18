from django.db import models
from datetime import datetime


class Entertainments(models.Model):
    start_data = models.DateTimeField(default=datetime.now(), verbose_name='Время и дата создания запроса.', null=True)
    category = models.CharField(max_length=100, verbose_name='Категория резвлечения.', null=True)
    entertainment = models.CharField(max_length=100, verbose_name='Развлечение.', null=True)
    participants = models.IntegerField(verbose_name='Количество участников.', null=True)
    price = models.FloatField(verbose_name='Цена.', null=True)
    accessibility = models.FloatField(verbose_name='Доступность.', null=True)
    entertainment_id = models.IntegerField(verbose_name='ID развлечения.', null=True)
    link = models.URLField(max_length=100, verbose_name='Ссылка', null=True)

