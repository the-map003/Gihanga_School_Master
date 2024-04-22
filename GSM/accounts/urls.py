<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.account, name="account"),
]
=======
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.login,name='login'),
    
]
>>>>>>> bb170f86388bbd95d77827c257d7c2d2c71e5855
