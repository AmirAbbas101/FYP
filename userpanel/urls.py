from django.urls import path

from . import views

urlpatterns = [
    path("", views.candidate_dashboard_view, name="candidate-dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/my-applications", views.job_applications_view, name="applications"),
    path("profile/jobs", views.findJobsView, name="find-jobs"),
    path("settings/", views.settings_view, name="settings"),
]