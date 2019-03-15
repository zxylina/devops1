# -*- coding: utf-8 -*-
from django.conf.urls import url, include
# from .views import idc_list, idc_detail, idc_list_v2, idc_detail_v2
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     url('^$', views.api_root),
#     url('^idc/$', views.idc_list, name='idc-list'),
#     url('^idc_v2/$', views.idc_list_v2),
#     url('^idc/(?P<pk>[0-9]+)/$', views.idc_detail, name='idc-detail'),
#     url('^idc_v2/(?P<pk>[0-9]+)/$', views.idc_detail_v2)
#     # url('^idc', idc_list),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

##########################  版本三   ############################
# urlpatterns = [
#     url("^$", views.api_root),
#     url("^idcs/$", views.IdcList.as_view(), name="idc-list"),
#     url("^idcs/(?P<pk>[0-9]+)/$", views.IdcDetail.as_view(), name="idc_detail")
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

##########################  版本四   ############################
# urlpatterns = [
#     url("^$", views.api_root),
#     url("^idcs/$", views.IdcList_V4.as_view(), name="idc-list"),
#     url("^idcs/(?P<pk>[0-9]+)/$", views.IdcDetail_V4.as_view(), name="idc_detail")
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

##########################  版本五   ############################
# urlpatterns = [
#     url("^$", views.api_root),
#     url("^idcs/$", views.IdcList_V5.as_view(), name="idc-list"),
#     url("^idcs/(?P<pk>[0-9]+)/$", views.IdcDetail_V5.as_view(), name="idc_detail")
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

##########################  版本六   ############################
# idc_list = views.IdcListViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# idc_detail = views.IdcListViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })
#
# urlpatterns = [
#     url("^$", views.api_root),
#     url("^idcs/$", idc_list, name="idc-list"),
#     url("^idcs/(?P<pk>[0-9]+)/$", idc_detail, name="idc_detail")
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

##########################  版本七   ############################
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("idcs", views.IdcViewset_v7)
urlpatterns = [
    url(r'^', include(route.urls))
]



