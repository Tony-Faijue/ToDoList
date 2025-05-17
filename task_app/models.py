from django.db import models

# import settings for user model
from django.conf import settings

# Create your models here.
class Task (models.Model):
    #allow tasks to be assoicated with a user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_desc = models.CharField(max_length = 10000)
    task_status = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name}, {self.task_desc}, {self.task_status}"


class Note (models.Model):
    note_id = models.AutoField(primary_key= True)
    note_name = models.CharField(max_length= 255)
    note_desc = models.CharField(max_length=2000)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.note_name}, {self.note_desc}"

