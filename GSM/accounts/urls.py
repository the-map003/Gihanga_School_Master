
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('redirect/',views.redirect_users , name='redirect_users'),
    path('master/',views.master_dash,name='master'),
    path('add_user/',views.create_user,name='create_user'),
    path('manage_user/',views.manage_user,name='manage_user'),
    path('report_user/',views.report_user,name='report_user'),
    # Add other URL patterns for your apps
]
