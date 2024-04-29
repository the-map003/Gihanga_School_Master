from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(DiscussionThread)


