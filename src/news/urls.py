from django.urls import path
from rest_framework.routers import DefaultRouter

from news.views import CommentViewSet, NewsViewSet

router = DefaultRouter()

router.register("news", NewsViewSet, basename="news")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("news/<pk>/comments/", CommentViewSet.as_view({"get": "list"})),
    path("news/<pk>/comments/<int:id>", CommentViewSet.as_view({"get": "retrieve"})),
] + router.urls
