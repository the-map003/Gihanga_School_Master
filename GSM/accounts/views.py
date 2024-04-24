from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
def login_user(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            print('user found')
            return redirect('redirect_users')
        else:
            # Handle invalid login (e.g., display an error message)
            print('user not found')
            return render(request, 'accounts/login.html', {'error_message': 'Invalid username or password'})
   
    return render(request, 'accounts/login.html')

@login_required
def redirect_users(request):
    user = request.user
    if user.role == Users.STORE_KEEPER:
        return redirect('stock_dash') 
    elif user.role == Users.DEAN_OF_STUDY:
        return redirect('student_admin') 
    else:
        # Handle default redirection (e.g., redirect to a generic dashboard)
        return redirect('student_dashboard')  # Replace 'generic_dashboard' with the appropriate URL name for the generic dashboard



def create_user(request):
    if request.method == 'POST':
        # Get the custom user model
        User = get_user_model()
        
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validate passwords
        if password1 != password2:
            messages.error(request,'Passwords do not match')
            return render(request, 'accounts/register.html')
        
        user = User(
            username=username,
            email=email,
            role=User.STUDENT,  
            phone_number='',  
            profile_picture=''  
        )
        
        # Hash the password
        user.set_password(password1)
        
        # Save the user
        user.save()
        messages.success(request, 'User registered successfully!')

        # Redirect to a success page or login page
        return redirect('login')  # Assuming you have a URL named 'login' for the login page
    
    return render(request, 'accounts/register.html')
