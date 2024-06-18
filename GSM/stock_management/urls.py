from django.contrib import admin
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_logout_view

urlpatterns = [
    path('',views.stock_dash, name="stock_dash"),
    path('add_supplier',views.add_supplier,name='add_supplier'),
    path('logout/', custom_logout_view, name='logout'),
    path('insert_supplier',views.insert_supplier,name='insert_supplier'),
    path('manage_supplier', views.manage_supplier, name="manage_supplier"),
    path('update_supplier/<int:supplier_id>/',views.update_supplier, name="update_supplier"),
    path('delete_supplier/<int:supplier_id>/',views.delete_supplier, name="delete_supplier"),
    path('report_supplier',views.report_supplier, name="report_supplier"),
    path('add_item', views.add_item, name="add_item"),
    path('manage_item', views.manage_item, name="manage_item"),
    path('update_item/<int:item_id>/<int:category_id>/', views.update_item, name="update_item"),
    path('delete_item/<int:item_id>/',views.delete_item, name="delete_item"),
    path('report_item',views.report_item, name="report_item"),
    path('make_order', views.make_order, name="make_order"),
    path('manage_order', views.manage_order, name="manage_order"),
    path('update_order/<int:purchaseorder_id>/<int:item_id>/<int:supplier_id>/', views.update_order, name="update_order"),
    path('delete_order/<int:purchaseorder_id>/',views.delete_order, name="delete_order"),
    path('report_order',views.report_order, name="report_order"),
    path('receive_order/<int:order_id>/', views.receive_order, name="receive_order"),
    path('stockin', views.stockin, name="stockin"),
    path('stockout', views.stockout, name="stockout"),
    path('manage_stockout', views.manage_stockout, name="manage_stockout"),
    path('update_stockout/<int:stockout_id>/<int:item_id>/<int:supplier_id>/', views.update_stockout, name="update_stockout"),
    path('delete_stockout/<int:stockout_id>/', views.delete_stockout, name='delete_stockout'),
    path('report_stock', views.report_stock, name="report_stock"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)