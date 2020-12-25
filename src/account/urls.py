from django.urls import path
from rest_framework.routers import DefaultRouter

from account.views import RegistrationViewSet, LogoutView, LoginView

router = DefaultRouter()

router.register(r"account", RegistrationViewSet, 'account')

urlpatterns = [
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
]

urlpatterns += router.urls
