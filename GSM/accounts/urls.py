
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('redirect/',views.redirect_users , name='redirect_based_on_role'),
    # Add other URL patterns for your apps
]