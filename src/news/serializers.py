from rest_framework.serializers import ModelSerializer

from news.models import News, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = News
        fields = ['comments']
