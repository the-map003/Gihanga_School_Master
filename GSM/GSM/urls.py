from django.contrib import admin
from django.urls import path,include
urlpatterns = [
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
