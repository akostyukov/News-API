from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

tz = timezone.get_default_timezone()


class News(models.Model):
    category = models.CharField("Категория", max_length=100)
    header = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст", max_length=1000)
    date_time = models.DateTimeField("Дата и время публикации")

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
        return f"{self.header} - {self.get_date_time()}"

    def get_date_time(self):
        return self.date_time.astimezone(tz).strftime("%d.%m.%Y %H:%M")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField("Текст", max_length=1000)
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)
    edited = models.BooleanField(verbose_name="Изменялось", default=False)

    def __str__(self):
        return (
            f"Комментарий от {self.author.username} под {self.news.header}: {self.text}"
        )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
