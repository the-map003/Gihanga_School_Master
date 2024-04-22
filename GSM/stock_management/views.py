from django.shortcuts import render

def stock_dash(request):
    return render(request,"stock_management/stock_dash.html")
