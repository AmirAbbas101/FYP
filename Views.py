from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LoginView(FormView):
    template_name = "users/login.html"  # Your login template
    form_class = AuthenticationForm
    success_url = reverse_lazy("dashboard")  # Redirect after successful login

    def form_valid(self, form):
        # Authenticate the user
        user = authenticate(
            request=self.request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )

        if user is not None:
            login(self.request, user)  # Login the user
            user.set_last_login()  # Update last login time
            messages.success(self.request, _("Login successful!"))

            # Redirect to the success URL
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, _("Invalid credentials, please try again."))
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Handle invalid form submission (e.g., incorrect credentials)
        messages.error(self.request, _("Invalid credentials, please try again."))
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        # Redirect logged-in users to the dashboard
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


from django.urls import path
from .views import (
    CustomLogoutView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    RegisterView,
    LoginView,
)

urlpatterns = [
    # Login and Register URLs
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    # Logout URL
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    # Password Reset URLs
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
