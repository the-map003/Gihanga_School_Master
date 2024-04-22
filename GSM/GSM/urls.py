"""
URL configuration for GSM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('announcements/',include('announcements_messaging.urls')),
    path('attendance/',include('attendance_management.urls')),
    path('fee/',include('fees_management.urls')),
    path('hardware/',include('fees_management.urls')),
    path('library/',include('library_management.urls')),
    path('report/',include('result_report_management.urls')),
    path('stock/',include('stock_management.urls')),
    path('student/',include('student_management.urls')),
    path('playground/',include('student_playground.urls')),
    path('timetable/',include('timetable_management.urls')),
]
