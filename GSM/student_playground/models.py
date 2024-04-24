from django.db import models
from accounts.models import Users

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

class ForumPost(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.club.name
