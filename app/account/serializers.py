from rest_framework import serializers
from .models import User


class RegisterAuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


