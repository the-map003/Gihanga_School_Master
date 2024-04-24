from django.shortcuts import render, redirect
from . models import Supplier
from django.contrib import messages

def stock_dash(request):
    return render(request,"stock_management/dash.html")

def add_supplier(request):
    return render(request,'stock_management/form_supplier.html')

def insert_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phonenumber = request.POST.get('phone')
        email = request.POST.get('email')
        insert = Supplier.objects.create(name=name, contact1=phonenumber, address=email)
        insert.save()
        messages.success(request, "Supplier Well Inserted!!")
        return redirect('insert_supplier')
    else:
        return render(request,'stock_management/form_supplier.html')

def manage_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'stock_management/manage_supplier.html', {'suppliers': suppliers})

def update_supplier(request, supplier_id):
    if request.method == 'POST':
        supplier = Supplier.objects.get(pk=supplier_id)
        supplier.name = request.POST['name']
        supplier.contact1 = request.POST['phone']
        supplier.address = request.POST['email']
        supplier.save()
        return redirect('manage_supplier')
    else:
        supplier = Supplier.objects.get(pk=supplier_id)
        return render(request, 'stock_management/update_supplier.html', {'supplier': supplier})
def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(pk=supplier_id)
    supplier.delete()
    return redirect('manage_supplier')

def report_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'stock_management/report_supplier.html', {'suppliers': suppliers})

def make_order(request):
    return render(request, 'stock_management/form_order.html')

def manage_order(request):
    return render(request, 'stock_management/manage_order.html')