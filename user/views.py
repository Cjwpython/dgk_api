from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer


@permission_classes((AllowAny,))
class UserCreateAPIView(generics.CreateAPIView):
    '''注册用户'''
    queryset = User.objects.all()
    serializer_class = UserSerializer