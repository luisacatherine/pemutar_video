from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile')
]