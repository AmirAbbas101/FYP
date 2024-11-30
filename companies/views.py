from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()
@login_required
def company_dashboard_view(request):
    page_name = "Dashboard"
    return render(request, 'companies/company-dashboard.html', {"page_name": page_name})

@login_required
def job_listing_view(request):
    page_name = "Job Listing"
    return render(request, 'companies/job-listing.html', {"page_name": page_name})