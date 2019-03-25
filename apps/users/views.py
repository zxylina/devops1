# -*- coding:utf8 -*-
from django.shortcuts import render
from rest_framework import viewsets
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from .serializers import UserSerializer

# Create your views here.
class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定用户信息
    list：
        返回用户列表
    get:
        list
        get
    create
    update
    delete
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

