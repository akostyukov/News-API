from rest_framework.routers import DefaultRouter

from news.views import NewsViewSet, CommentViewSet

router = DefaultRouter()

router.register('', NewsViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
