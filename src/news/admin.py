from django.contrib import admin

from news.models import Comment, News

admin.site.register(News)
admin.site.register(Comment)
