from django.db import models
from accounts.models import Users

# Create your models here.
class Class(models.Model):
    name=models.CharField(max_length=255)
    section=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    student_class=models.ForeignKey(Class,related_name='student',on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    dob=models.DateField()
    student_id=models.CharField(max_length=255)
    father_name=models.CharField(max_length=255)
    mother_name=models.CharField(max_length=255)
    p_number=models.CharField(max_length=255)
    s_number=models.CharField(max_length=255)
    # username=models.ForeignKey(Users,related_name='username',on_delete=models.CASCADE,null=True)
    # password=models.ForeignKey(Users,related_name='password',on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    image=models.ImageField(upload_to='stdimg',blank=True,null=True)
    registered_by=models.ForeignKey(Users,related_name='student',on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)


class Notice(models.Model):
    title=models.CharField(max_length=255)
    nclass=models.ForeignKey(Class,related_name='notice',on_delete=models.CASCADE)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    creator=models.ForeignKey(Users,related_name='user',on_delete=models.CASCADE)

class Pnotice(models.Model):
    title=models.CharField(max_length=255)
    
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    creator=models.ForeignKey(Users,related_name='puser',on_delete=models.CASCADE)


class Pages(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    creator=models.ForeignKey(Users,related_name='nuser',on_delete=models.CASCADE)








