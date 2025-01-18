from django.urls import include, path

from work import views


urlpatterns = [
    path("", views.emp, name="emp"),
    
]
