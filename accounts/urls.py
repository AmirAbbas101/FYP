# from django.urls import path

# from . import views

# urlpatterns = [
#     path("login/", views.login_view, name="login"),
#     path("logout/", views.logout_view, name="logout"),
#     path("register/", views.register_view, name="register"),
# ]

from django.urls import path
from .views import (
    LogoutView,
    register_view,
    # RegisterView,
    login_view,
    ForgotPasswordView,
    PasswordResetSentView,
    ResetPasswordView,
    CustomPasswordResetDoneView,
)

urlpatterns = [
    # Login and Register URLs
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    # path("register/", RegisterView.as_view(), name="register"),
    # Logout URL
    path("logout/", LogoutView, name="logout"),
    # Password Reset URLs
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path(
        "password-reset-sent/<uuid:reset_id>/",
        PasswordResetSentView.as_view(),
        name="password-reset-sent",
    ),
    path(
        "reset-password/<uuid:reset_id>/",
        ResetPasswordView.as_view(),
        name="reset-password",
    ),
    path(
        "reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
]
