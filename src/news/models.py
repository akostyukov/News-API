from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    category = models.CharField('Категория', max_length=100)
    header = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст', max_length=1000)
    # date_time = models.DateTimeField('Дата публикации', default='2020-12-25 12:00')
    # time = models.TimeField('Время публикации', default=datetime.now())

    def __str__(self):
        return f'{self.header}'
