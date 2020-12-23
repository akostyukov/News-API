from rest_framework.serializers import HyperlinkedModelSerializer

from news.models import News


class NewsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
