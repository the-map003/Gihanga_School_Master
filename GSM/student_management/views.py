from django.shortcuts import render,redirect
# from .forms import*
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

from django.contrib.auth.decorators import login_required

# Create your views here.
def StudentDashboard(request):

    return render(request,'student_management/student_dash.html')
def StudentAdmin(request):
    
    return render(request,'student_management/student_admin_dash.html')
# def StudentAbout(request):
#     return render(request,'sdata/about.html')
# def StudentContact(request):
#     return render(request,'sdata/contact.html')
# def StudentAdminLogin(request):
#     if request.user.is_authenticated:
#         return redirect('stddashboard')
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
        
#         user=User.objects.get(username=username)
        
            
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('stddashboard')
       

#     return render(request,'sdata/admin/login.html')

# def Dashboard(request):
#     Classes=Class.objects.all()
#     students=Student.objects.all()
    
#     notices=Notice.objects.all()
#     pnotices=Pnotice.objects.all()
#     context={'Classes':Classes,'students':students,'notices':notices,'pnotices':pnotices}
#     return render(request,'sdata/admin/dashboard.html',context)

# def logoutUser(request):
#     logout(request)
#     return redirect('stdindex')
# def Addclass(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         section=request.POST.get('section')
#         Class.objects.create(name=name,section=section)
        

#     return render(request,'sdata/admin/add-class.html')

# # views.py
# def Manageclass(request):
#     Classes=Class.objects.all()
#     context={'Classes':Classes}
#     return render(request,'sdata/admin/manage-class.html',context)

# def AddStudent(request):
#     Classes=Class.objects.all()
#     if request.method=='POST':
#         name=request.POST.get('stuname')
#         email=request.POST.get('stuemail')
#         stclass=request.POST.get('stuclass')
#         stdc=Class.objects.get(name=stclass)
#         gender=request.POST.get('gender')
#         dob=request.POST.get('dob')
#         fname=request.POST.get('fname')
#         mname=request.POST.get('mname')
#         stid=request.POST.get('stuid')
#         stimg=request.POST.get('image')
#         stnumber=request.POST.get('connum')
#         gnumber=request.POST.get('altconnum')
#         username=request.POST.get('uname')
#         password=request.POST.get('password')
#         user=request.user.id
#         address=request.POST.get('address')
#         Student.objects.create(name=name,email=email,student_class=stdc,
#                              gender=gender,dob=dob,student_id=stid,
#                              father_name=fname,s_number=stnumber,p_number=gnumber,
#                              username=username,password=password,location=address,
#                              mother_name=mname,registered_by=User(user))

        
#     context={'Classes':Classes}
#     return render(request,'sdata/admin/add-students.html',context)

# def ManageStudent(request):
#     students=Student.objects.all()

#     context={'students':students}
#     return render(request,'sdata/admin/manage-students.html',context)


# def AddNotice(request):
#     clses=Class.objects.all()
#     if request.method=='POST':
#         title=request.POST.get('title')
#         message=request.POST.get('message')
#         nclass=request.POST.get('nclass')
#         nc=Class.objects.get(name=nclass)
#         user=request.user.id
#         Notice.objects.create(title=title,nclass=nc,creator=User(user),message=message)

#     return render(request,'sdata/admin/add-notice.html',{'clses':clses})

# def ManageNotice(request):
#     students=Notice.objects.all()

#     context={'students':students}
#     return render(request,'sdata/admin/manage-notice.html',context)


# def ManagepNotice(request):
#     students=Pnotice.objects.all()

#     context={'students':students}
#     return render(request,'sdata/admin/manage-public-notice.html',context)


# def AddpNotice(request):
#     clses=Class.objects.all()
#     if request.method=='POST':
#         title=request.POST.get('title')
#         message=request.POST.get('message')
       
#         user=request.user.id
#         Pnotice.objects.create(title=title,creator=User(user),message=message)

#     return render(request,'sdata/admin/add-public-notice.html',{'clses':clses})

# def Report(request):
#     return render(request,'sdata/admin/between-dates-reports.html')
# def Search(request):
#     q=request.POST.get('q') 
#     if q != None:
#         student=Student.objects.filter(
#         Q(student_id__icontains=q)|
#         Q(name__icontains=q)|
#         Q(father_name__icontains=q)|
#         Q(mother_name__icontains=q)
#         ) 
#     else:
#         return render(request,'sdata/admin/search.html',{'q':q})


#     return render(request,'sdata/admin/search.html',{'student':student,'q':q})


# def StudentUserLogin(request):
#     if request.user.is_authenticated:
#         return redirect('stduserdashboard')
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
        
#         user=User.objects.get(username=username)
        
            
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('stduserdashboard')
       

#     return render(request,'sdata/admin/login.html')


# def UserDashboard(request):

#     return render(request,'sdata/user/dashboard.html')

# def UserNotice(request):
#     students=Notice.objects.all()

#     context={'students':students}
#     return render(request,'sdata/user/view-notice.html',context)




