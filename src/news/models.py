from django.db import models


class News(models.Model):

    category = models.CharField("Категория", max_length=100)
    header = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст", max_length=1000)
    date_time = models.CharField('Дата и время публикации', max_length=200)

    def __str__(self):
        return f"{self.header} - {self.date_time}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
