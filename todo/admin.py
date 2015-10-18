from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('name', 'assigned_to', 'done', 'created', 'modified')

