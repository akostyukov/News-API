from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from account.serializers import RegistrationSerializer


class RegistrationViewSet(ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
