from django.contrib import admin
from .models import Task, TaskStatus, Comments

# Register your models here.
admin.site.register(Task, TaskStatus, Comments)
