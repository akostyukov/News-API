from django.contrib import admin

from v1.news.models import Comment, News

admin.site.register(News)
admin.site.register(Comment)
