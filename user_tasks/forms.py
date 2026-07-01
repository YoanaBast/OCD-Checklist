from django import forms
from user_tasks.models import Task, UserTaskTracker


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']



class CompleteTaskForm(forms.ModelForm):
    class Meta:
        model = UserTaskTracker
        fields = ["notes"]
        widgets = {
            "notes": forms.TextInput(
                attrs={"placeholder": "Optional notes..."}
            )
        }