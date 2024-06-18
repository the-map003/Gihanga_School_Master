from django.db import models
from accounts.models import Users

class Author(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) 

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_available = models.IntegerField()
    def __str__(self) -> str:
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    date_due = models.DateField()
    def __str__(self) -> str:
        return self.book.title
