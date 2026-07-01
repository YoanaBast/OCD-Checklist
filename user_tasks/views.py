from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView

from user_tasks.models import UserTaskTracker, Task
from user_tasks.forms import TaskForm, CompleteTaskForm


# Create your views here.

class DashboardView(LoginRequiredMixin, ListView):
    model = UserTaskTracker
    template_name = "dashboard.html"
    context_object_name = "trackers"

    def get_queryset(self):
        return (
            UserTaskTracker.objects.filter(
                task__user=self.request.user
            )
            .select_related("task")
            .order_by("-last_completed")
        )

@login_required
def profile(request):
    trackers = UserTaskTracker.objects.filter(
        task__user=request.user
    ).select_related('task')

    return render(request, 'user_tasks/profile.html', {
        'trackers': trackers
    })


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():

            task = form.save(commit=False)
            task.user = request.user
            task.save()

            UserTaskTracker.objects.create(task=task)

            return redirect("profile")
    else:
        form = TaskForm()

    return render(request, 'user_tasks/add_task.html', {'form': form})


@login_required
def delete_task(request, tracker_id):
    tracker = get_object_or_404(
        UserTaskTracker,
        id=tracker_id,
        task__user=request.user
    )

    if request.method == 'POST':
        tracker.delete()
        return redirect('profile')

@login_required
def edit_task(request, tracker_id):
    tracker = get_object_or_404(
        UserTaskTracker,
        id=tracker_id,
        task__user=request.user
    )

    task = tracker.task

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = TaskForm(instance=task)

    return render(request, "user_tasks/edit_task.html", {
        "form": form,
    })


@login_required
def complete_task(request, tracker_id):
    tracker = get_object_or_404(
        UserTaskTracker,
        id=tracker_id,
        task__user=request.user
    )

    if request.method == "POST":
        form = CompleteTaskForm(request.POST, instance=tracker)

        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.last_completed = timezone.now()
            tracker.save()

            return redirect("dashboard")
    else:
        form = CompleteTaskForm(instance=tracker)

    return render(request, "user_tasks/complete_task.html", {
        "form": form,
        "tracker": tracker,
    })