from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_profile_view, name="dashboard"),
    path("profile/<int:user_id>", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),
]