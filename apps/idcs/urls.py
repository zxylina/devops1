from django.conf.urls import url
from .views import idc_list, idc_detail, idc_list_v2, idc_detail_v2
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('^idc/$', idc_list),
    url('^idc_v2/$', idc_list_v2),
    url('^idc/(?P<pk>[0-9]+)/$', idc_detail),
    url('^idc_v2/(?P<pk>[0-9]+)/$', idc_detail_v2)
    # url('^idc', idc_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)