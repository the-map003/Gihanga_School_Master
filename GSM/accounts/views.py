from django.shortcuts import render

def login(request): 
    return render(request, 'accounts/login.html')

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Users

@login_required
def redirect_users(request):
    user = request.user
    if user.role == Users.MASTER:
        return redirect('master_app:index')  # Replace 'master_app:index' with the appropriate URL name for the master app
    elif user.role == Users.DEAN_OF_STUDY:
        return redirect('dean_of_study_app:index')  # Replace 'dean_of_study_app:index' with the appropriate URL name for the dean of study app
    elif user.role == Users.ACCOUNTANT:
        return redirect('accountant_app:index')  # Replace 'accountant_app:index' with the appropriate URL name for the accountant app
    # Add more elif conditions for other roles
    else:
        # Handle default case (e.g., redirect to a generic dashboard)
        return redirect('generic_dashboard')  # Replace 'generic_dashboard' with the appropriate URL name for the generic dashboard

# Example URL configuration in urls.py

