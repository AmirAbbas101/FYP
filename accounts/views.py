from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CandiddateModel

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        login_identifier = request.POST.get("login")  # Could be username or email
        password = request.POST.get("password")
        selected_role = request.POST.get(
            "role"
        )  # Role selected (e.g., "RE" for Recruiter, "CA" for Candidate)

        # Try to authenticate with username
        user = authenticate(request, username=login_identifier, password=password)

        # If no match with username, attempt email-based authentication
        if user is None:
            user_by_email = User.objects.filter(email=login_identifier).first()
            if user_by_email:
                user = authenticate(
                    request, username=user_by_email.username, password=password
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
                    return redirect("recruiter")
                elif selected_role == "CA":
                    return redirect("candidate")
            else:
                messages.error(
                    request, "The role you selected does not match your account."
                )
        else:
            messages.error(request, "Invalid username/email or password.")

        return redirect("login")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")  # Replace 'login' with the name of your login page URL


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname", "")
        last_name = request.POST.get("lastname", "")
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_img", None)  # Optional profile image
        selected_role = request.POST.get(
            "role"
        )  # User role (e.g., "CA" for Candidate, "RE" for Recruiter)
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
        return redirect("login")
    return render(request, "accounts/register.html")


@login_required
def user_profile_view(request):
    """Display user profile information."""
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def recruiter_dashboard_view(request):
    """Dashboard view for candidates."""
    return render(request, "accounts/recruiter_dashboard.html")


@login_required
def candidate_dashboard_view(request):
    try:
        # Try to get the candidate profile associated with the logged-in user
        candidate_profile = CandiddateModel.objects.get(user_id=request.user.user_id)
    except CandiddateModel.DoesNotExist:
        # If the profile doesn't exist, redirect to the candidate registration form
        return redirect(
            "candidate-settings"
        )  # Use your candidate registration URL name here

    # If the candidate profile exists, show the dashboard
    return render(
        request,
        "accounts/candidate_dashboard.html",
        {"candidate_profile": candidate_profile},
    )


def recruiter_settings_view(request):
    return render(request, "accounts/recruiter_settings.html")


@login_required
def candidate_settings_view(request):
    if request.method == "POST":
        # Get the current user (who is registering as a candidate)
        current_user = request.user

        # Collect form data from the request
        phone_number = request.POST.get("phone")
        address = request.POST.get("address")
        skills = request.POST.get("skills", "")
        education = request.POST.get("education", "")
        experience = request.POST.get("experience", "")
        resume = request.FILES.get("resume", None)

        # Check if the user already has a candidate profile
        (current_user.user_id,)
        if CandiddateModel.objects.filter(user_id=current_user).exists():
            # You may choose to redirect or show an error if a profile already exists
            return redirect("candidate")  # Redirect to candidate dashboard

        # Create a new candidate profile
        CandiddateModel.objects.create(
            user_id=current_user,  # Link the candidate profile to the current user
            phone=phone_number,
            address=address,
            skills=skills,
            education=education,
            experience=experience,
            resume=resume,
        )
        return redirect("candidate")

    return render(request, "accounts/candidate_settings.html")
