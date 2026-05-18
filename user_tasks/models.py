from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"user id: {self.user}, task: {self.task}"

class UserTaskTracker(models.Model):
    user_task = models.ForeignKey(UserTask, on_delete=models.CASCADE)
    last_completed = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        result = f"{self.user_task.task} last completed at {self.last_completed}"
        if self.notes:
            result += f"\nNotes: {self.notes}"

        return result
