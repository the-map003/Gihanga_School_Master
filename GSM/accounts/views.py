from django.shortcuts import render

def login(request): 
    return render('accounts/login.html')

