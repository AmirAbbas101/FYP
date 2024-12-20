from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        login_identifier = request.POST.get("login")
        password = request.POST.get("password")
        selected_role = request.POST.get(
            "role"
        )  # Role selected (e.g., "RE" for Recruiter, "CA" for Candidate)

        # Try to authenticate with user_name
        user = authenticate(request, user_name=login_identifier, password=password)

        # If no match with user_name, attempt email-based authentication
        if user is None:
            user_by_email = User.objects.filter(email=login_identifier).first()
            if user_by_email:
                user = authenticate(
                    request, user_name=user_by_email.user_name, password=password
                )

        # Authentication check and role validation
        if user is not None:
            if (
                user.role == selected_role
            ):  # Ensure that the selected role matches the user's role
                login(request, user)
                messages.success(request, "Login successful!")
                # Redirect based on role
                if selected_role == "RE":
                    return redirect("candidate-dashboard")
                elif selected_role == "CA":
                    return redirect("candidate-dashboard")

            else:
                messages.error(
                    request, "The role you selected does not match your account."
                )
        else:
            messages.error(request, "Invalid user_name/email or password.")

        return redirect("login")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")  # Replace 'login' with the name of your login page URL


def register_view(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_img", None)  # Optional profile image
        selected_role = request.POST.get(
            "role"
        )  # User role (e.g., "CA" for Candidate, "RE" for Recruiter)
        password = request.POST.get("password")

        validation_errors = []

        # Validate uniqueness of user_name
        if User.objects.filter(user_name=user_name).exists():
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
            user_name=user_name,
            email=email,
            profile_img=profile_image,
            role=selected_role,
            password=password,
        )

        messages.success(request, "Account created successfully. Please log in.")

        # Redirect based on role or default to login
        return redirect("login")
    return render(request, "accounts/register.html")
