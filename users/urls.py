# users/urls.py
import django.contrib.admin
from django.urls import path, include

from .views import dashboard, register, activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("register/", register, name="register"),
    # path('login/', login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path("verify_email/<uidb64>/<token>/", Email_Verify.as_view(), name='confirm_email'),
    # path('verification/', include('verify_email')),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]