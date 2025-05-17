from django.contrib import admin
from task_app.models import Task, Note

# Register your models here.
admin.site.register(Task)
admin.site.register(Note)