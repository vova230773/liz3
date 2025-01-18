from django.urls import include, path

from order import views


urlpatterns = [
    path("", views.order, name="orders"),
    path("user/", include("users.urls", namespace="user")),
    path("podatkoviykalendar/", views.podkal, name="podkal"),
]
