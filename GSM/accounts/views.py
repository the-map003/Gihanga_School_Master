
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

@login_required
def redirect_users(request):
    user = request.user
    if user.role == Users.STORE_KEEPER:
        return redirect('stock_management:stock_dash')  
