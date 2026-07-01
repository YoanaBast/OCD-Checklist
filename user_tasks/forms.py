from django import forms
from user_tasks.models import Task, UserTaskTracker


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data["name"]
        user = self.initial.get("user")

        if Task.objects.filter(user=user, name=name).exists():
            raise forms.ValidationError("You already have a task with this name.")

        return name

class CompleteTaskForm(forms.ModelForm):
    class Meta:
        model = UserTaskTracker
        fields = ["notes"]
        widgets = {
            "notes": forms.TextInput(
                attrs={"placeholder": "Optional notes..."}
            )
        }