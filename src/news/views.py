from rest_framework.viewsets import ModelViewSet

from news.models import News, Comment
from news.serializers import NewsSerializer, CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
