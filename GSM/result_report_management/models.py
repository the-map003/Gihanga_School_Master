from django.db import models
from student_management.models import Student

class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self) -> str:
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self) -> str:
        return self.student.name
