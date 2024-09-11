"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core.api import LizPOST, LizViewSet,LizViewSet2
      
from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter

from core.serializers import LizSerializer


app_name = 'core'
router = DefaultRouter()
router.register(r'liz',LizPOST)

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('company/<slug:company_slug>/', views.Company.as_view(), name='company'), 
    path('create-company/', views.CreateCompany.as_view(), name='create_company'),
    path('upload_resume/',views.upload_resume.as_view(), name = "files" ),
    path('create-user/', views.CreateUser.as_view(), name='create_user'),
    path('vvid/', views.vvid.as_view(), name='vvid'),
    
    re_path('^liz/(?P<guid>.+)/$', LizViewSet.as_view({'get': 'list'})),
    re_path('^lz/(?P<okpo>.+)/$', LizViewSet2.as_view({'get': 'list'})),
    
    
    

]
urlpatterns += router.urls






