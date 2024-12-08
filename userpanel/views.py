from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import Candidate

User = get_user_model()


@login_required
def candidate_dashboard_view(request):
    page_name = "Dashboard"
    return render(request, "userpanel/dashboard.html", {"page_name": page_name})


@login_required
def profile_view(request):
    user = get_object_or_404(User, pk=request.user.user_id)
    data = Candidate.objects.get(user_id=request.user.user_id)

    page_name = "My Profile"
    return render(
        request,
        "userpanel/profile.html",
        {"page_name": page_name, "user": user, "data": data},
    )


def findJobsView(request):
    return render(request, "userpanel/jobs.html", {"page_name": "Find Jobs"})


@login_required
def settings_view(request):
    return render(
        request,
        "userpanel/settings.html",
        {"page_name": "Settings", "active_section": "my_profile"},
    )


def job_applications_view(request):
    return render(
        request, "userpanel/my-applications.html", {"page_name": "My Applications"}
    )
