from django.shortcuts import render, redirect
from accounts.models import Users
from django.contrib import messages
from .models import Author, Category
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from datetime import datetime

@login_required
def library_dash(request):
    return render(request, 'library_management/dashboard/library_dash.html')

@login_required
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
 
@login_required   
def manage_author(request):
    author = Author.objects.all()
    return render(request, 'library_management/author/manage_author.html', {'author':author})

@login_required
def update_author(request,author_id):
    if request.method == 'POST':
        author=Author.objects.get(pk=author_id)
        author.name = request.POST['name']
        author.save()
        return redirect('manage_author')
    else:
        author = Author.objects.get(pk=author_id)
    return render(request, 'library_management/author/update_author.html', {'author':author})

@login_required
def delete_author(request,author_id):
    author = Author.objects.get(pk=author_id)
    author.delete()
    return redirect('manage_author')

