from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class RegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        user = User(username=self.validated_data["username"])

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        user.set_password(password)
        user.save()

        return user
