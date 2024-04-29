
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from.import views

urlpatterns = [
 
    path('', views.login_user, name='login'),
    # Path to Django's built-in login view with your custom template
    path('built-in-login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='built-in-login'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('redirect/',views.redirect_users , name='redirect_users'),
    path('master/',views.master_dash,name='master'),
    path('add_user/',views.create_user,name='create_user'),
    path('manage_user/',views.manage_user,name='manage_user'),
    path('report_user/',views.report_user,name='report_user'),
    path('logout/', views.user_logout, name='custom_logout'),

]
