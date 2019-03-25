"""devops1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.idcs.views import IdcViewset_v7
from users.views import UserViewset
from cabinet.views import CabinetViewset
from manufacturer.views import ManufacturerViewset, ProductViewset
from servers.views import ServerAutoReportViewset, NetworkDeviceViewset, IPViewset, ServerViewset
from rest_framework.documentation import include_docs_urls


# urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', include("apps.idcs.urls"))
# ]

route = DefaultRouter()
route.register("idcs", IdcViewset_v7, base_name='idcs')
route.register("users", UserViewset, base_name='users')
route.register("cabinet", CabinetViewset, base_name='cabinet')
route.register("Manufacturer", ManufacturerViewset, base_name='Manufacturer')
route.register("Product", ProductViewset, base_name='Product')
route.register("ServerAutoReport", ServerAutoReportViewset, base_name='ServerAutoReport')
route.register("NetworkDevice", NetworkDeviceViewset, base_name='NetworkDevice')
route.register("IP", IPViewset, base_name='IP'),
route.register("Servers", ServerViewset, base_name='Servers')

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^docs/', include_docs_urls("51reboot接口文档"))
]
