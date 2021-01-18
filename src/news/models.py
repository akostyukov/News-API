from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    category = models.CharField("Категория", max_length=100)
    header = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст", max_length=1000)
    date_time = models.CharField("Дата и время публикации", max_length=200)
    likes = models.ManyToManyField(
        User, blank=True, related_name="likes", verbose_name="Оценили"
    )
    comments = models.ManyToManyField(
        User,
        blank=True,
        related_name="comments",
        through="Comment",
        verbose_name="Комментарии",
    )

    def __str__(self):
        return f"{self.header} - {self.date_time}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField("Текст", max_length=1000)
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Комментарий от {self.author.username} под {self.news.header}: {self.text}"
        )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
