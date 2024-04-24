from django.urls import path
from .import views
urlpatterns=[
    path('',views.StudentDashboard,name='student_dashboard'),
    path('admin/',views.StudentAdmin,name='student_admin'),
    # path('contact/',views.StudentContact,name='stdcontact'),
    # path('admin/',views.StudentAdminLogin,name='stdlogin'),
    # path('admin/dashboard/',views.Dashboard,name='stddashboard'),
    # path('admin/dashboard/addclass/',views.Addclass,name='addclass'),
    # path('admin/dashboard/manageclass/',views.Manageclass,name='manageclass'),
    # path('admin/dashboard/addstudent/',views.AddStudent,name='addstudent'),
    # path('admin/dashboard/managestudent/',views.ManageStudent,name='managestudent'),
    # path('admin/dashboard/addnotice/',views.AddNotice,name='addnotice'),
    # path('admin/dashboard/managenotice/',views.ManageNotice,name='managenotice'),
    # path('admin/dashboard/addpnotice/',views.AddpNotice,name='addpnotice'),
    # path('admin/dashboard/managepnotice/',views.ManagepNotice,name='managepnotice'),
    # path('admin/dashboard/report/',views.Report,name='report'),
    # path('admin/dashboard/search/',views.Search,name='search'),
    # path('logOut/',views.logoutUser,name="logout"),
    # path('publicnotice/<str:pk>/',views.Viewpn,name='pnoticeindex'),
    # path('user/',views.StudentUserLogin,name='stduserlogin'),
    # path('user/dashboard/',views.UserDashboard,name='stduserdashboard'),
    # path('user/dashboard/viewnotice',views.UserNotice,name='viewstdnotice'),


]
