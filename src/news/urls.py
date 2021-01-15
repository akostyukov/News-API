from rest_framework.routers import DefaultRouter

from news.views import CommentViewSet, NewsViewSet

router = DefaultRouter()

router.register("news", NewsViewSet, basename="news")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = router.urls
