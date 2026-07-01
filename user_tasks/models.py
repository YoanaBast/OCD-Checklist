from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name="unique_task_name_per_user")
        ]

    def __str__(self):
        return self.name



class UserTaskTracker(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    last_completed = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        result = f"{self.task} last completed at {self.last_completed}"
        if self.notes:
            result += f"\nNotes: {self.notes}"
        return result