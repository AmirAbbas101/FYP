from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        login_identifier = request.POST.get("login")  # Could be username or email
        password = request.POST.get("password")
        selected_role = request.POST.get("role")  # Role selected (e.g., "RE" for Recruiter, "CA" for Candidate)

        # Try to authenticate with username
        user = authenticate(request, username=login_identifier, password=password)
        
        # If no match with username, attempt email-based authentication
        if user is None:
            user_by_email = User.objects.filter(email=login_identifier).first()
            if user_by_email:
                user = authenticate(request, username=user_by_email.username, password=password)

        # Authentication check and role validation
        if user is not None:
            if user.role == selected_role:  # Ensure that the selected role matches the user's role
                login(request, user)
                messages.success(request, "Login successful!")
                # Redirect based on role
                if selected_role == "RE":
                    return redirect("recruiter_dashboard")
                elif selected_role == "CA":
                    return redirect("candidate_dashboard")
            else:
                messages.error(request, "The role you selected does not match your account.")
        else:
            messages.error(request, "Invalid username/email or password.")

        return redirect("login")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_image", None)  # Optional profile image
        selected_role = request.POST.get("role")  # User role (e.g., "CA" for Candidate, "RE" for Recruiter)
        password = request.POST.get("password")

        validation_errors = []

        # Validate uniqueness of username
        if User.objects.filter(username=username).exists():
            validation_errors.append("Username is already taken.")

        # Validate uniqueness of email
        if User.objects.filter(email=email).exists():
            validation_errors.append("Email is already registered.")

        # Ensure password is of a valid length
        if len(password) < 5:
            validation_errors.append("Password must be at least 5 characters long.")

        # If there are validation errors, return them
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)
            return redirect("register")

        # Create new user
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            profile_img=profile_image,
            role=selected_role,
            password=password,
        )

        messages.success(request, "Account created successfully. Please log in.")
        
        # Redirect based on role or default to login
        return redirect("home" if selected_role == "RE" else "login")

    return render(request, "accounts/register.html")


@login_required
def user_profile_view(request):
    """Display user profile information."""
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def candidate_dashboard_view(request):
    """Dashboard view for candidates."""
    return render(request, "accounts/candidate_dashboard.html")


@login_required
def recruiter_dashboard_view(request):
    """Dashboard view for recruiters."""
    return render(request, "accounts/recruiter_dashboard.html")
