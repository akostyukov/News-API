from rest_framework.routers import DefaultRouter

from account.views import RegistrationViewSet

router = DefaultRouter()

router.register(r"", RegistrationViewSet)

urlpatterns = router.urls
