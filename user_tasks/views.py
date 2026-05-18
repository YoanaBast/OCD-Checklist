from django.shortcuts import render
from django.views.generic import ListView

from user_tasks.models import UserTaskTracker


# Create your views here.
class DashboardView(ListView):
    model = UserTaskTracker
    template_name = "dashboard.html"
    context_object_name = "dashboard_tasks"