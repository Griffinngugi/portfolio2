from django.contrib import admin

# Register your models here.
from .models import students,teachers,Staff

admin.site.register(students)

admin.site.register(teachers)

admin.site.register(Staff)
