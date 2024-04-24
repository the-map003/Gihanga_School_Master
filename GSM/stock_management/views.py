from django.shortcuts import render

def stock_dash(request):
    return render(request,"stock_management/dash.html")


def add_supplier(request):
    return render(request,'stock_management/form_supplier.html')

def manage_supplier(request):
    return render(request, 'stock_management/manage_supplier.html')

def make_order(request):
    return render(request, 'stock_management/form_order.html')

def manage_order(request):
    return render(request, 'stock_management/manage_order.html')