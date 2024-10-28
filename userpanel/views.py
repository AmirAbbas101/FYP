from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import CandiddateModel

User = get_user_model()

@login_required
def dashboard_profile_view(request):
    page_name = "Dashboard"
    return render(request, 'userpanel/dashboard-profile.html', {"page_name": page_name})

@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    data = CandiddateModel.objects.get(user_id=user_id)


    page_name = "My Profile"
    return render(request, 'userpanel/profile.html', {
        "page_name": page_name,
        "user": user,
        "data":data
    })

@login_required
def settings_view(request):
    return render(request, 'userpanel/settings.html', {"page_name":"Settings", 'active_section': 'my_profile'})
