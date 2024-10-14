
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('core/', include('core.urls',namespace='core')),
    path('order/', include(('order.urls','order'),namespace='order')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete'),
    path('', include('social_django.urls', namespace='social')),
    path('', include('users.urls',namespace='user')),
    path('zak/',views.zakaz.as_view() , name='zakaz'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL='https://localhost:8000/api/auth/complete/google-oauth2/'
LOGOUT_REDIRECT_URL = 'https://localhost:8000/api/auth/complete/google-oauth2/'






