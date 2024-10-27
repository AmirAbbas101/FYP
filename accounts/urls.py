from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("recruiter/", views.recruiter_dashboard_view, name="recruiter"),
    path("candidate/", views.candidate_dashboard_view, name="candidate"),
    path(
        "recruiter-settings/", views.recruiter_settings_view, name="recruiter-settings"
    ),
    path(
        "candidate-settings/", views.candidate_settings_view, name="candidate-settings"
    ),
    path("profile/", views.user_profile_view, name="profile"),
]
