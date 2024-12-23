from django.shortcuts import render
from jobs.models import Job


def home_view(request):
    featured_jobs = Job.featured_jobs()
    jobs = Job.all_jobs()
    companies = ["intel", "intel", "intel", "intel"]
    page_name = "home"
    context = {
        "jobs": jobs,
        "featured_jobs": featured_jobs,
        "companies": companies,
        "page_name": page_name,
    }
    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")
