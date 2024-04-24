
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('redirect/',views.redirect_users , name='redirect_users'),
    path('register/',views.create_user,name='create_user'),
    # Add other URL patterns for your apps
]
