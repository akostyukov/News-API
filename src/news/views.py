from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from news.models import Comment, News
from news.permissions import IsOwnerOrStaffOrReadOnly
from news.serializers import CommentSerializer, NewsSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes_by_action = {
        "partial_update": [IsOwnerOrStaffOrReadOnly],
        "destroy": [IsOwnerOrStaffOrReadOnly],
    }

    def get_queryset(self):
        print(self.request.version)
        return Comment.objects.filter(news=self.kwargs["news_pk"])

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]


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
