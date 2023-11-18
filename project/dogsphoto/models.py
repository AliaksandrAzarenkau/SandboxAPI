from django.db import models

from datetime import datetime


class DogsPhoto(models.Model):
    start_data = models.DateTimeField(default=datetime.now(), null=True, verbose_name='Дата создания')
    message = models.URLField(max_length=255, verbose_name="Ссылка на фото")
    status = models.CharField(verbose_name="Статус ответа", max_length=100)
    