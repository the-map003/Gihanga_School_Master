from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from student_management.models import Student,Teacher
import os
from django.conf import settings
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
    elif user.role == Users.MASTER:
        return redirect('master')
    else:
        # Handle default redirection (e.g., redirect to a generic dashboard)
        return redirect('student_dashboard')  # Replace 'generic_dashboard' with the appropriate URL name for the generic dashboard


@login_required


def create_user(request):
    user_role_choices = Users.ROLE_CHOICES
    
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        role = request.POST.get('role')
        gender = request.POST.get('gender')  # Assuming the form includes a 'gender' field
        
        # Validate passwords
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/register.html', {'user_role_choices': user_role_choices})

        if Users.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'accounts/register.html', {'user_role_choices': user_role_choices})

        # Determine profile picture path based on gender
        base_dir = settings.BASE_DIR  # Get the base directory of the Django project
        if gender == 'male':
            profile_picture = os.path.join(base_dir, 'profile_pictures/men.jpg')  # Construct the profile picture path for male
        elif gender == 'female':
            profile_picture = os.path.join(base_dir, 'profile_pictures/women.jpg')  # Construct the profile picture path for female
        else:
            profile_picture = os.path.join(base_dir, 'profile_pictures/men.jpg')  # Construct the profile picture path for default image
        
        # Create user object
        User = get_user_model()
        user = User(
            first_name=fname,
            last_name=lname,
            username=username,
            email=email,
            role=role,  
            phone_number='',  
            profile_picture=profile_picture  # Set the profile picture path
        )
        user.set_password(password1)  # Hash the password
        try:
            user.save()
        except Exception as e:
            print(e)




        if role == '6':
            try:
                teacher = Teacher.objects.create(user=user)
            except Exception as e:
                print(e)
            
        elif role == '7':
            try:
                student = Student.objects.create(user=user, registered_by=request.user)
            except Exception as e:
                print(e)
            
        messages.success(request, 'User registered successfully!')
        return redirect('manage_user')  # Redirect to login page after successful registration

    return render(request, 'accounts/register.html', {'user_role_choices': user_role_choices})


def master_dash(request):

    return render(request,'accounts/master_dash.html')

from django.shortcuts import render
from .models import Users  # Assuming your Users model is in the same app

def manage_user(request):
    users = Users.objects.all()
    for user in users:
        user.role_label = user.get_role_label()  # Assign role label to each user
    context = {'users': users}
    return render(request, 'accounts/manage_users.html', context)

def report_user(request):
    return
