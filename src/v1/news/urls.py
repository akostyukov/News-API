from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from v1.news.views import CommentViewSet, NewsViewSet

router = SimpleRouter()
router.register(r"news", NewsViewSet, basename="news")

news_router = NestedSimpleRouter(router, r"news", lookup="news")
news_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = router.urls + news_router.urls
