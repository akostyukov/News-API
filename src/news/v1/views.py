from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from news.models import Comment, News
from news.permissions import IsOwnerOrStaffOrReadOnly
from news.serializers import (
    CommentSerializer,
    NewsSerializer,
    NewsWithoutEditingSerializer,
)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(news=self.kwargs["news_pk"])

    def perform_update(self, serializer):
        serializer.save(edited=True)


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["category", "date_time"]
    search_fields = ["header"]

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        news = News.objects.get(id=pk)

        if news.likes.filter(id=self.request.user.id).exists():
            news.likes.remove(self.request.user)
            return Response({"success": "Like has been removed"})
        else:
            news.likes.add(self.request.user)
            return Response({"success": "Like has been set"})

    @action(detail=True, methods=["get"], url_path="likes")
    def get_likes(self, request, pk=None):
        news = News.objects.get(id=pk)
        return Response(
            {"likes": [f"{user.username}({user.id})" for user in news.likes.all()]}
        )

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == "PUT" or self.request.method == "PATCH":
            serializer_class = NewsWithoutEditingSerializer

        return serializer_class
