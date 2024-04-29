from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Users
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from student_management.models import Student,Teacher,Class,Course
import os
from django.conf import settings

@login_required
def StudentDashboard(request):

    return render(request,'student_management/student/student_dash.html')

@login_required
def Dos(request):
    
    return render(request,'student_management/dos/dos_dash.html')
@login_required
def Teachers(request):
    
    return render(request,'student_management/dos/dos_dash.html')
@login_required

def DosManageStudent(request):
    students = Student.objects.all()
    for student in students:
        # Assuming there's a user field on the Student model
        user = student.user
        user.role_label = user.get_role_label()  # Assuming get_role_label() is a method on the User model
    context = {'students': students}
    return render(request, 'student_management/dos/manage_student.html', context)


def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        syllabus = request.FILES.get('syllabus')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        duration = request.POST.get('duration')
        teachers_ids = request.POST.getlist('teachers')
        
        # Convert teachers IDs to Teacher objects
        teachers = Teacher.objects.filter(id__in=teachers_ids)
        
        # Create the course object
        course = Course.objects.create(
            name=name,
            description=description,
            syllabus=syllabus,
            start_date=start_date,
            end_date=end_date,
            duration=duration
        )
        
        # Add teachers to the course
        course.teachers.add(*teachers)
        
        return redirect('course_list')  # Redirect to the course list page after adding the course
    
    # If it's a GET request or form is not valid, render the add course template
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'student_management/dos/add_course.html', context)


@login_required
def DosAddStudent(request):
    classes=Class.objects.all()
  
    
    if request.method == 'POST':
        # Retrieve form data
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        father_name = request.POST.get('father')
        city = request.POST.get('city')
        mother_name = request.POST.get('mother')
        p_phone = request.POST.get('p_phone')
        s_phone = request.POST.get('s_phone')
        img = request.POST.get('img')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password1')
        student_class=request.POST.get('student_class')
        std_class=Class.objects.get(id=student_class)
        
       
        gender = request.POST.get('gender')  # Assuming the form includes a 'gender' field
        
        # Validate passwords
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/register.html')

        if Users.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'accounts/register.html')

        # Determine profile picture path based on gender
        if not img:
            base_dir = settings.BASE_DIR  # Get the base directory of the Django project
            if gender == 'male':
                profile_picture = os.path.join(base_dir, 'profile_pictures/men.jpg')  # Construct the profile picture path for male
            elif gender == 'female':
                profile_picture = os.path.join(base_dir, 'profile_pictures/women.jpg')  # Construct the profile picture path for female
            else:
                profile_picture = os.path.join(base_dir, 'profile_pictures/men.jpg')  # Construct the profile picture path for default image
        else:
            profile_picture=img    
        # Create user object
        User = get_user_model()
        user = User(
            first_name=fname,
            last_name=lname,
            username=username,
            email=email,
            
            role=7,  
            
            profile_picture=profile_picture  # Set the profile picture path
        )
        user.set_password(password1)  # Hash the password
        
        user.save()
        


        
        Student.objects.create(user=user,student_class=std_class,p_number=p_phone,s_number=s_phone,
                                            
                                                      
                                                    
                                                    gender=gender,
                                                    mother_name=mother_name,
                                                    father_name=father_name, 
                                                    location=city, 
                                                    registered_by=request.user)
      
            
        messages.success(request, 'User registered successfully!')
        return redirect('manage_user')  # Redirect to login page after successful registration


    
    return render(request,'student_management/dos/add_student.html',{'classes':classes})


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




