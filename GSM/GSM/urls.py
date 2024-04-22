from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path,include
>>>>>>> bb170f86388bbd95d77827c257d7c2d2c71e5855

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
<<<<<<< HEAD
=======
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
>>>>>>> bb170f86388bbd95d77827c257d7c2d2c71e5855
]
