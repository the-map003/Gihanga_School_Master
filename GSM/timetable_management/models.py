from django.db import models
from student_management.models import Class

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class ClassSchedule(models.Model):
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self) -> str:
        return self.class_attended
