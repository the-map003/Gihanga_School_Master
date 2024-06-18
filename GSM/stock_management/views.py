from django.shortcuts import render, redirect
from . models import Supplier, Category, Item, PurchaseOrder, Stock_In, Stock_Out
from django.contrib import messages
from accounts.models import Users
from datetime import datetime
from django.utils.dateparse import parse_date
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

def stock_dash(request):
    return render(request,"stock_management/dash.html")

def add_supplier(request):
    return render(request,'stock_management/form_supplier.html')

def insert_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phonenumber = request.POST.get('phone')
        email = request.POST.get('email')
        
        # Check if a supplier with the same name or email already exists
        try:
            existing_supplier = Supplier.objects.get(contact1=phonenumber)
            messages.error(request, "Supplier with this Phone number already exists!")
            return redirect('insert_supplier')
        except ObjectDoesNotExist:
            pass  # If no supplier with the same name is found, proceed with insertion
        
        try:
            existing_supplier = Supplier.objects.get(address=email)  # Assuming 'address' is unique for suppliers
            # If a supplier with the same email already exists, display a message or handle it as needed
            messages.error(request, "Supplier with this email already exists!")
            return redirect('insert_supplier')
        except ObjectDoesNotExist:
            pass  # If no supplier with the same email is found, proceed with insertion
        
        # If no duplicate is found, proceed with insertion
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
        
        # Check if an item with the same name and category already exists
        try:
            category = Category.objects.get(name=categor)
        except Category.DoesNotExist:
            category = Category.objects.create(name=categor)
        
        try:
            existing_item = Item.objects.get(name=name, category=category)
            # If an item with the same name and category already exists, display a message or handle it as needed
            messages.error(request, "An item with this name and category already exists!")
        except Item.DoesNotExist:
            # If no duplicate item is found, proceed with insertion
            try:
                Item.objects.create(name=name, category=category, price=price, description=description, created_by=request.user)
                messages.success(request, "Item successfully added!")
            except Exception as e:
                print(e)
    
    context = {'categories': categories}
    return render(request, 'stock_management/form_item.html', context)

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
        total_amount = quantity * price
        
        try:
            # Retrieve the User object using the user_id
            user = Users.objects.get(id=user_id)
            
            # Retrieve the Item and Supplier objects
            item = Item.objects.get(name=items)
            supplier = Supplier.objects.get(name=supply)
            
            # Check if a purchase order with the same item, supplier, and user already exists
            existing_order = PurchaseOrder.objects.filter(item=item, supplier=supplier, creator=user)
            if existing_order.exists():
                # If a duplicate order is found, display a message or handle it as needed
                messages.error(request, "Duplicate purchase order detected!")
            else:
                # If no duplicate order is found, create a new PurchaseOrder object
                PurchaseOrder.objects.create(item=item, supplier=supplier, quantity=quantity, unit=price, creator=user, total=total_amount)
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


def receive_order(request, order_id):
    try:
        order = PurchaseOrder.objects.get(id=order_id)
    except PurchaseOrder.DoesNotExist:
        messages.error(request, "Failed to receive order. Purchase order not found.")
        return redirect('manage_order')  # Redirect to an error page or handle as needed

    # Update the status of the purchase order
    order.status = True  # Assuming True means received
    order.save()

    # Now, create a Stock_In entry for the received order
    Stock_In.objects.create(
        supplier=order.supplier,
        item=order.item,  # Assuming a single item per order
        quantity=order.quantity,
        unit=order.unit,
        total=order.total,
        creator=order.creator,
        status="Received",  # You can set the status as needed
    )

    messages.success(request, "Order received successfully and added to stock.")
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

def stockin(request):
    stockin = Stock_In.objects.all()
    return render(request, 'stock_management/stock_in.html',{'stockins':stockin})

def stockout(request):
    item_var = Item.objects.all()
    supplier_var = Supplier.objects.all()

    if request.method == 'POST':
        item_name = request.POST.get('item')
        supplier_name = request.POST.get('supplier')
        quantity = int(request.POST.get('quantity'))
        
        try:
            # Check if there's a Stock_In entry for the selected item and supplier
            stock_in_item = Stock_In.objects.get(item__name=item_name, supplier__name=supplier_name)
            if 0 <= quantity <= stock_in_item.quantity:
                stock_in_item.quantity -= quantity
                stock_in_item.total = stock_in_item.quantity * stock_in_item.unit  # Update the total
                stock_in_item.save()

                # Create a Stock_Out entry
                user_id = request.user.id
                user = Users.objects.get(id=user_id)
                item = Item.objects.get(name=item_name)
                supplier = Supplier.objects.get(name=supplier_name)
                total = quantity * stock_in_item.unit
                Stock_Out.objects.create(item=item, supplier=supplier, quantity=quantity, unit=stock_in_item.unit, total=total, creator=user, status="Stocked Out")

                messages.success(request, "Stock OUT created successfully!")
                return redirect('stockout')
            else:
                messages.error(request, "Invalid quantity for stock out")
        except Stock_In.DoesNotExist:
            messages.error(request, f"No Stock IN entry found for item '{item_name}' supplied by '{supplier_name}'. Please create a Stock IN entry first.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            print(e)

    context = {
        'item_var': item_var,
        'supplier_var':supplier_var
    }
    return render(request, 'stock_management/stock_out.html', context)

def manage_stockout(request):
    stockout = Stock_Out.objects.all()
    return render(request, 'stock_management/manage_stockout.html',{'stockouts':stockout})

def update_stockout(request, stockout_id, item_id, supplier_id):
    stockout = Stock_Out.objects.get(pk=stockout_id)
    item = Item.objects.get(pk=item_id)
    supplier = Supplier.objects.get(pk=supplier_id)

    if request.method == 'POST':
        try:
            new_quantity = float(request.POST['quantity'])
            
            # Retrieve the corresponding Stock_In entry
            stockin = Stock_In.objects.get(item=item, supplier=supplier)
            
            # Ensure the new quantity doesn't exceed the available stock or go below zero
            if new_quantity <= stockin.quantity and new_quantity >= 0:
                # Calculate the difference in quantity
                quantity_diff = new_quantity - stockout.quantity

                # Update the Stock_Out entry
                stockout.quantity = new_quantity
                
                # Update the total price in Stock_Out
                stockout.total = new_quantity * stockout.unit
                stockout.updated_at=Stock_Out.updated_at
                stockout.save()

                # Update the quantity and total in Stock_In
                stockin.quantity -= quantity_diff
                stockin.total = stockin.quantity * stockin.unit
                stockin.save()

                messages.success(request, "Stock OUT updated successfully!")
                return redirect('manage_stockout')  # Redirect to the appropriate view
            else:
                messages.error(request, "Quantity cannot exceed available stock or be negative.")
        except (ValueError, Stock_In.DoesNotExist):
            messages.error(request, "Invalid input or no corresponding Stock IN entry found.")

    context = {
        'stockout': stockout,
        'item': item,
        'supplier': supplier,
    }
    return render(request, 'stock_management/update_stockout.html', context)

def delete_stockout(request, stockout_id):
    stockout = Stock_Out.objects.get(pk=stockout_id)
    stockout.delete()
    messages.success(request, "Stockout succes")
    return redirect('manage_stockout')

def report_stock(request):
    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        report_type = request.POST.get('report_type')

        # Default to today's date if start_date and end_date are not provided
        if not start_date_str:
            start_date = timezone.now().date()
        else:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        
        if not end_date_str:
            end_date = timezone.now().date()
        else:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        if report_type == 'stockin':
            # Query Stock_In entries within the date range
            stock_entries = Stock_In.objects.filter(stocked_at__date__range=[start_date, end_date])
            report_title = 'Stock In Report'
        elif report_type == 'stockout':
            # Query Stock_Out entries within the date range
            stock_entries = Stock_Out.objects.filter(stocked_at__date__range=[start_date, end_date])
            report_title = 'Stock Out Report'
        else:
            # Invalid report type, return an empty queryset
            stock_entries = []
            report_title = ''

        context = {
            'report_title': report_title,
            'stock_entries': stock_entries,
        }
        return render(request, "stock_management/report_stock.html", context)
    else:
        return render(request, "stock_management/report_stock.html")



