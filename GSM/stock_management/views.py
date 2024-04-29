from django.shortcuts import render, redirect
from . models import Supplier, Category, Item, PurchaseOrder
from django.contrib import messages
from accounts.models import Users
from datetime import datetime
from django.utils.dateparse import parse_date

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
    if request.method == 'POST':
        # Parse start and end dates from the form submission
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        # Parse the date strings into date objects
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        # If start or end date is not provided, default to today's date
        if not start_date:
            start_date = datetime.now().date()
        if not end_date:
            end_date = datetime.now().date()
        # Filter items based on the date range
        suppliers = Supplier.objects.filter(created__date__range=[start_date, end_date])
        return render(request, 'stock_management/report_supplier.html', {'suppliers': suppliers})
    else:
        # If it's a GET request or if no dates are provided, display an empty form
        return render(request, 'stock_management/report_supplier.html', {})

def add_item(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('itemname')
        categor = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        user = request.user.id
        category, created_at=Category.objects.get_or_create(name=categor)
        try:
            Item.objects.create(name=name, category=category, price=price, description=description, created_by=Users(user))
            messages.success(request, "Item successful added!")
        except Exception as e:
            print(e)

    context={'categories':categories}
    return render(request,'stock_management/form_item.html',context)

def manage_item(request):
    item = Item.objects.all()
    return render(request, 'stock_management/manage_item.html', {'items': item})

def update_item(request, item_id, category_id):
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        item.name = request.POST['itemname']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        category= Category.objects.get(pk=category_id)
        category.name = request.POST['category']
        category.save()
        return redirect('manage_item')
    else:
        item = Item.objects.get(pk=item_id)
        category = Category.objects.get(pk=category_id)
        return render(request, 'stock_management/update_item.html',{'item':item})
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('manage_item')

def report_item(request):
    if request.method == 'POST':
        # Parse start and end dates from the form submission
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        # Parse the date strings into date objects
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        # If start or end date is not provided, default to today's date
        if not start_date:
            start_date = datetime.now().date()
        if not end_date:
            end_date = datetime.now().date()
        # Filter items based on the date range
        items = Item.objects.filter(created_at__date__range=[start_date, end_date])
        return render(request, 'stock_management/report_item.html', {'items': items})
    else:
        # If it's a GET request or if no dates are provided, display an empty form
        return render(request, 'stock_management/report_item.html', {})

def make_order(request):
    item_var = Item.objects.all()
    supplier_var = Supplier.objects.all()
    
    if request.method == 'POST':
        supply = request.POST.get('supplier')
        items = request.POST.get('item')
        quantity = float(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        user_id = request.user.id
        total_amount= quantity*price
        
        try:
            # Retrieve the User object using the user_id
            user = Users.objects.get(id=user_id)
            
            # Retrieve the Item and Supplier objects
            itemss = Item.objects.get(name=items)
            suppliers = Supplier.objects.get(name=supply)
            
            # Create a PurchaseOrder object
            PurchaseOrder.objects.create(item=itemss, supplier=suppliers, quantity=quantity, unit=price, creator=user,total=total_amount)
            messages.success(request, "Purchase Order created successfully!")
            return redirect('make_order')
        except Item.DoesNotExist:
            messages.error(request, f"Item '{items}' does not exist.")
        except Supplier.DoesNotExist:
            messages.error(request, f"Supplier '{supply}' does not exist.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            print(e)
            
    context = {
        'item_var': item_var,
        'supplier_var': supplier_var
    }
    return render(request, 'stock_management/form_order.html', context)

def manage_order(request):
    purchaseorder = PurchaseOrder.objects.all()
    return render(request, 'stock_management/manage_order.html', {'purchaseorders':purchaseorder})

def update_order(request, purchaseorder_id, item_id, supplier_id):
    # Retrieve the purchaseorder regardless of the request method
    purchaseorder = PurchaseOrder.objects.get(pk=purchaseorder_id)
    item = Item.objects.get(pk=item_id)
    supplier = Supplier.objects.get(pk=supplier_id)
    
    if request.method == 'POST':
        # Update the purchaseorder with data from the POST request
        purchaseorder.quantity = request.POST['quantity']
        purchaseorder.unit = request.POST['price']
        item.name = request.POST['item']
        supplier.name = request.POST['supplier']
        
        # Calculate the total
        quantity = float(request.POST['quantity'])
        price = float(request.POST['price'])
        total = quantity * price
        
        # Update the total field of the purchaseorder
        purchaseorder.total = total
        
        purchaseorder.save()
        item.save()
        supplier.save()
        
        return redirect('manage_order')
    else:
        return render(request, 'stock_management/update_order.html', {'purchaseorder': purchaseorder})

def delete_order(request, purchaseorder_id):
    purchaseorder = PurchaseOrder.objects.get(pk=purchaseorder_id)
    purchaseorder.delete()
    return redirect('manage_order')

def report_order(request):
    if request.method == 'POST':
        # Parse start and end dates from the form submission
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        # Parse the date strings into date objects
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
        # If start or end date is not provided, default to today's date
        if not start_date:
            start_date = datetime.now().date()
        if not end_date:
            end_date = datetime.now().date()
        # Filter items based on the date range
        purchaseorder = PurchaseOrder.objects.filter(ordered_at__date__range=[start_date, end_date])
        return render(request, 'stock_management/report_order.html', {'purchaseorders': purchaseorder})
    else:
        # If it's a GET request or if no dates are provided, display an empty form
        return render(request, 'stock_management/report_item.html', {})
