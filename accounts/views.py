from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    return render(request, "home.html")


def registerView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        profile_img = request.FILES.get(
            "profile_img"
        )  # Changed to request.FILES for handling file uploads
        role = request.POST.get("role")
        password = request.POST.get("password")

        user_data_has_error = False

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")

        # Ensure password is valid (at least 5 characters long in this example)
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters long")

        # If there are errors, redirect to the registration page
        if user_data_has_error:
            return redirect("register")
        else:
            # Create a new user
            new_user = User.objects.create_user(
                username=username,
                email=email,
                profile_img=profile_img,
                role=role,
                password=password,
            )
            messages.success(
                request, "Account created successfully. You can now log in."
            )

            # Redirect user based on role
            if role == "EP":
                return redirect("home")
            elif role == "JB":
                pass

    return render(request, "accounts/register.html")
