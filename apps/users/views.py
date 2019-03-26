# -*- coding:utf8 -*-
from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.pagination import PageNumberPagination
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter

User = get_user_model()
from .serializers import UserSerializer
# from .pagination import Pagination

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
    # pagination_class = PageNumberPagination
    # pagination_class = Pagination

    # def get_queryset(self):
    #     queryset = super(UserViewset, self).get_queryset()
    #     username = self.request.query_params.get("username", None)
    #     if username:
    #         queryset = queryset.filter(username__icontains=username)
    #     return queryset
    # filter_backends = (DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ("username",)

