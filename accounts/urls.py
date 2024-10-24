from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path('recruiter-registeration/', views.recruiter_registeration_view, name='recruiter-registeration'),
    path('candidate-registeration/', views.candidate_registeration_view, name='candidate-registeration'),
    path("login/", views.login_view, name="login"),
    path('candidate/', views.candidate_dashboard_view, name='candidate_dashboard'),
    path('recruiter/', views.recruiter_dashboard_view, name='recruiter_dashboard'),
    path('profile/', views.user_profile_view, name='profile'),
]
