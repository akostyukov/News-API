from rest_framework.viewsets import ModelViewSet

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
