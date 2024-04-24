from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class Schedule(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
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
        return self.device.name
