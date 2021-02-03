from rest_framework.serializers import ModelSerializer

from news.models import Comment, News


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsWithoutEditingSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ["header", "category"]
