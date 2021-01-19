from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from news.models import Comment, News
from news.serializers import CommentSerializer, NewsSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["category", "date_time"]
    search_fields = ["header"]
