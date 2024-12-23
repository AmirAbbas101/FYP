from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import PasswordReset
from django.views.generic import FormView, TemplateView

from django.utils.translation import gettext as _
from .forms import PasswordResetForm, SetNewPasswordForm
from django.contrib.auth.views import PasswordResetDoneView


User = get_user_model()


def login_view(request):
    user = None
    if request.method == "POST":
        login_data = request.POST.get("login")  # Could be username or email
        password = request.POST.get("password")
        selected_role = request.POST.get("role")

        # Try to authenticate with username
        user = authenticate(request, username=login_data, password=password)

        # If no match with username, attempt email-based authentication
        if user is None:
            user_by_email = User.objects.filter(email=login_data).first()
            if user_by_email:
                user = authenticate(
                    request, username=user_by_email.username, password=password
                )

        # Authentication check and role validation
        if user is not None:
            if user.role == selected_role:
                login(request, user)
                user.set_last_login()
                messages.success(request, _("Login successful!"))
                # Redirect based on the selected role
                if selected_role == "RE":  # Recruiter role
                    return redirect(reverse_lazy("home"))
                elif selected_role == "CA":  # Candidate role
                    return redirect(reverse_lazy("candidate-dashboard"))
                else:
                    return redirect(reverse_lazy("home"))
            else:
                messages.error(
                    request, "The role you selected does not match your account."
                )
        else:
            messages.error(request, "Invalid username/email or password.")

        return redirect(reverse_lazy("login"))

    return render(request, "accounts/login.html")


def LogoutView(request):
    logout(request)
    return redirect("login")
    # return render(request, "accounts/logout.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_img", None)  # Optional profile image
        password = request.POST.get("password")
        selected_role = request.POST.get("role")

        validation_errors = []

        # Validate uniqueness of username
        if User.objects.filter(username=username).exists():
            validation_errors.append("Username is already taken.")

        # Validate uniqueness of email
        if User.objects.filter(email=email).exists():
            validation_errors.append("Email is already registered.")

        # Ensure password is of a valid length
        if len(password) < 8:
            validation_errors.append("Password must be at least 8 characters long.")

        # If there are validation errors, return them
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)
            return redirect("register")

        # Create new user
        User.objects.create_user(
            # first_name=first_name,
            # last_name=last_name,
            username=username,
            email=email,
            profile_img=profile_image,
            role=selected_role,
            password=password,
        )
        print(
            f"\n\n\n\n\nusername = {username}\nemail = {email}\nrole = {selected_role}\nprofile_img = {profile_image}\npassword = {password}\n\n\n\n"
        )
        messages.success(request, "Account created successfully. Please log in.")

        # Redirect based on role or default to login
        return redirect("login")
    return render(request, "accounts/register.html")


class ForgotPasswordView(FormView):
    template_name = "accounts/forgot_password.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("password-reset-sent")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        try:
            user = User.objects.get(email=email)
            password_reset = PasswordReset.objects.create(user=user)

            # Create password reset URL
            reset_url = reverse(
                "reset-password", kwargs={"reset_id": password_reset.reset_id}
            )
            full_reset_url = (
                f"{self.request.scheme}://{self.request.get_host()}{reset_url}"
            )

            # Send email
            subject = _(f"Hi {user.username}")
            email_body = _(
                f"Click the link below to reset your password:\n\n{full_reset_url}"
            )
            email_message = EmailMessage(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email_message.send(fail_silently=True)

            return redirect("password-reset-sent", reset_id=password_reset.reset_id)
        except User.DoesNotExist:
            messages.error(self.request, _("No user with that email found."))
            return self.form_invalid(form)


class PasswordResetSentView(TemplateView):
    template_name = "accounts/password_reset_done.html"

    def get(self, request, *args, **kwargs):
        reset_id = kwargs.get("reset_id")
        if not PasswordReset.objects.filter(reset_id=reset_id).exists():
            messages.error(self.request, _("Invalid reset ID."))
            return redirect("forgot-password")
        return super().get(request, *args, **kwargs)


class ResetPasswordView(FormView):
    template_name = "accounts/password_reset.html"
    form_class = SetNewPasswordForm
    success_url = reverse_lazy("password_reset_done")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reset_id = self.kwargs.get("reset_id")
        context["reset_id"] = reset_id
        return context

    def form_valid(self, form):
        reset_id = self.kwargs.get("reset_id")
        try:
            password_reset = PasswordReset.objects.get(reset_id=reset_id)

            if password_reset.is_expired:
                messages.error(self.request, _("Reset link has expired."))
                password_reset.delete()
                return redirect("forgot-password")

            # Update user password
            user = password_reset.user
            user.set_password(form.cleaned_data.get("password"))
            user.save()

            # Clean up reset entry
            password_reset.delete()
            messages.success(self.request, _("Password has been reset. Please login."))
            return super().form_valid(form)
        except PasswordReset.DoesNotExist:
            messages.error(self.request, _("Invalid reset ID."))
            return redirect("forgot-password")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"
