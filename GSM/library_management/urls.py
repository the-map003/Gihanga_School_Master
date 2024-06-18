from django.contrib import admin
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.library_dash, name="library_dashboard"),
    path('add_author', views.add_author, name="add_author"),
    path('manage_author', views.manage_author, name='manage_author'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)