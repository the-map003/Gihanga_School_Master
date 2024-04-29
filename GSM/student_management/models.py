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
    user=models.OneToOneField(Users,on_delete=models.CASCADE,related_name='student',null=True)
    student_class=models.ForeignKey(Class,related_name='student',on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=255)
   
    student_id=models.CharField(max_length=255)
    father_name=models.CharField(max_length=255,null=True)
    mother_name=models.CharField(max_length=255)
    p_number=models.CharField(max_length=255)
    s_number=models.CharField(max_length=255)
    # username=models.ForeignKey(Users,related_name='username',on_delete=models.CASCADE,null=True)
    # password=models.ForeignKey(Users,related_name='password',on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
 
    registered_by=models.ForeignKey(Users,related_name='student_reg',on_delete=models.CASCADE,null=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.user.first_name


class Teacher(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE,related_name='teacher',null=True)
   
    Teacher_class=models.ForeignKey(Class,related_name='teach_class',on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=255)
    
    Teacher_id=models.CharField(max_length=255)
    
    phone_number=models.CharField(max_length=255)
    
    # username=models.ForeignKey(Users,related_name='username',on_delete=models.CASCADE,null=True)
    # password=models.ForeignKey(Users,related_name='password',on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
  
    registered_by=models.ForeignKey(Users,related_name='teacher_reg',on_delete=models.CASCADE,null=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.user.first_name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    syllabus = models.FileField(upload_to='syllabus/', null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in weeks")
    teachers = models.ManyToManyField(Teacher, related_name='courses')

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)

class Submission(models.Model):
    student = models.ForeignKey(Student, related_name='submissions', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, related_name='submissions', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/')
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class DiscussionThread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='discussion_threads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



