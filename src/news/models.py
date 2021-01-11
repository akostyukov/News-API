from django.db import models


class News(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
