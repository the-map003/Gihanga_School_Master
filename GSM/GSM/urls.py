from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'stock_management'  # Define the app namespace
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

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)