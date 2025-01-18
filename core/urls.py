from django.contrib import admin
from django.urls import path, include, re_path
from core.api import (
    LizPOST,
    LizViewSet,
    LizViewSet2,
    OrderPOST,
    OrderViewSet,
    empDW,
    empViewSet,
    employeesPOST,
    mgPOST,
    posViewSet,
    postingPOST,
)

from django.urls import path
from core import views

from rest_framework import routers

from core.serializers import LizSerializer


app_name = "core"
router = routers.DefaultRouter()
router.register(r"liz", LizPOST)
router.register(r"mg", mgPOST)
router2 = routers.DefaultRouter()
router2.register(r"emp", employeesPOST)
router3 = routers.DefaultRouter()
router3.register(r"pos", postingPOST)
router4 = routers.DefaultRouter()
router4.register(r"ord", OrderPOST)

urlpatterns = [
    path("", views.Main.as_view(), name="main"),
    path("admin/", admin.site.urls),
    path("company/<slug:company_slug>/", views.Company.as_view(), name="company"),
    path("create-company/", views.CreateCompany.as_view(), name="create_company"),
    path("upload_resume/", views.upload_resume.as_view(), name="files"),
    path("create-user/", views.CreateUser.as_view(), name="create_user"),
    path("vvid/", views.vvid.as_view(), name="vvid"),
    re_path("^liz/(?P<guid>.+)/$", LizViewSet.as_view({"get": "list"})),
    re_path("^lz/(?P<okpo>.+)/$", LizViewSet2.as_view({"get": "list"})),
    re_path("^ordget/(?P<guid>.+)/$", OrderViewSet.as_view({"get": "list"})),
    path("", include(router2.urls)),
    path("", include(router3.urls)),
    path("", include(router4.urls)),
    path("news/", views.news_list, name="news_list"),
    path("news/create/", views.create_news, name="create_news"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    re_path("^empget/(?P<guid>.+)/$", empViewSet.as_view({"get": "list"})),
    re_path("^posget/(?P<guid>.+)/$", posViewSet.as_view({"get": "list"})),
]
urlpatterns += router.urls
