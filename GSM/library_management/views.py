from django.shortcuts import render, redirect
from accounts.models import Users
from django.contrib import messages
from .models import Author, Category
from django.core.exceptions import ObjectDoesNotExist

def library_dash(request):
    return render(request, 'library_management/dashboard/library_dash.html')

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            existing_author = Author.objects.get(name=name)
            messages.error(request, "Author wtih this name already exist!")

        except ObjectDoesNotExist:
            insert = Author.objects.create(name=name)
            insert.save()
            messages.success(request, "Author Well Inserted!!")
            return redirect('add_author')
    else:
        return render(request,'library_management/author/add_author.html')
    
def manage_author(request):
    author = Author.objects.all()
    return render(request, 'library_management/author/manage_author.html', {'authors':author})
