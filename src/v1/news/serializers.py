from rest_framework.serializers import ModelSerializer

from v1.news.models import Comment, News


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
