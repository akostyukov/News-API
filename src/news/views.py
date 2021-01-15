from rest_framework.viewsets import ModelViewSet

from news.models import Comment, News
from news.serializers import CommentSerializer, NewsSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        news = self.kwargs.get("pk")
        comments = Comment.objects.filter(news_id=news)
        return comments

    def get_object(self):
        queryset = self.get_queryset()
        comment = queryset.get(id=self.kwargs.get("id"))
        return comment


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
