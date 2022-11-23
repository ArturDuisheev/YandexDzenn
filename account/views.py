from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import RegisterAuthorSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterAuthorSerializer
