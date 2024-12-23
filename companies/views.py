from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from jobs.models import Job
from .models import Company


User = get_user_model()


@login_required
def company_dashboard_view(request):
    page_name = "Dashboard"
    return render(request, "companies/company-dashboard.html", {"page_name": page_name})


@login_required
def job_listing_view(request):
    page_name = "Job Listing"
    return render(request, "companies/job-listing.html", {"page_name": page_name})


def postJobView(request):
    if request.method == "POST":
        job_title = request.POST.get("job-title")
        job_description = request.POST.get("job-description")
        job_type = request.POST.get("job-type")
        location = request.POST.get("location")
        salary_range = request.POST.get("salary-range")
        experience_level = request.POST.get("experience-level")
        skills_required = request.POST.get("skills-required")
        application_deadline = request.POST.get("application-deadline")
        job_category = request.POST.get("job-category")
        responsibilities = request.POST.get("responsibilities")
        is_featured = request.POST.get("is-featured")

        Job.objects.create(
            job_title=job_title,
            job_description=job_description,
            job_type=job_type,
            location=location,
            salary_range=salary_range,
            experience_level=experience_level,
            skills_required=skills_required,
            application_deadline=application_deadline,
            job_category=job_category,
            responsibilities=responsibilities,
            is_featured=is_featured,
        )
    context = {"page_name": "Job Listing"}
    return render(request, "companies/post-new-job.html", context)


def settings_view(request, company_id):
    company = get_object_or_404(Company, company_id)
    return render(request, 'companies/settings.py')