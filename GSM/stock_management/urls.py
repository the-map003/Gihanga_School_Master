from django.contrib import admin
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.stock_dash, name="stock_dash"),
    path('add_supplier',views.add_supplier,name='add_supplier'),
    path('manage_supplier', views.manage_supplier, name="manage_supplier"),
    path('make_order', views.make_order, name="make_order"),
    path('manage_order', views.manage_order, name="manage_order"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)