<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Users

def login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('redirect_users')
        else:
            # Handle invalid login (e.g., display an error message)
            return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')
=======
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Users
>>>>>>> 418191de5a02d4eb6bbcd0133eaf3bbc70c83c04

def login(request): 
    return render(request, 'accounts/login.html')

@login_required
def redirect_users(request):
    user = request.user
    if user.role == Users.STORE_KEEPER:
        return redirect('stock_management:stock_dash')  
