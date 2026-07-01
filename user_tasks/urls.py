from django.urls import path
from .views import DashboardView, profile, add_task, delete_task, edit_task, complete_task


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("profile/", profile, name="profile"),
    path("add-task/", add_task, name="add_task"),
    path("delete-task/<int:tracker_id>/", delete_task, name="delete_task"),
    path("tasks/<int:tracker_id>/edit/", edit_task, name="edit_task"),
    path("tasks/<int:tracker_id>/complete/", complete_task, name="complete_task"),

]