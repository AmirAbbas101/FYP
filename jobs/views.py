from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Job
from companies.models import Company
from accounts.decorators import recruiter


from django.http import HttpResponsePermanentRedirect
from django.utils.text import slugify


class JobListView(ListView):
    model = Job
    template_name = "jobs/browse-jobs.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.all_jobs()


# class JobDetailView(DetailView):
#     model = Job
#     template_name = "jobs/job_detail.html"
#     context_object_name = "job"

#     def get_object(self, queryset=None):
#         job = super().get_object(queryset)
#         expected_slug = slugify(job.job_title)

#         # Check if the slug matches
#         if self.kwargs["job_title"] != expected_slug:
#             correct_url = reverse(
#                 "job-detail", kwargs={"job_id": job.job_id, "job_title": expected_slug}
#             )
#             return HttpResponsePermanentRedirect(correct_url)

#         return job


def JobDetailView(request, job_id, job_title):
    job = get_object_or_404(Job, job_id=job_id)
    expected_slug = slugify(job.job_title)
    if job_title != expected_slug:
        correct_url = reverse(
            "job-detail", kwargs={"job_id": job.job_id, "job_title": expected_slug}
        )
        return HttpResponsePermanentRedirect(correct_url)

    context = {"job": job}
    return render(request, "jobs/job_detail.html", context)


@login_required
@recruiter
def post_job_view(request, user_id):
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
        positions = request.POST.get("positions")
        requirements = request.POST.get("requirements")
        is_featured = request.POST.get("is-featured")
        employer = request.user
        company = get_object_or_404(Company, user=employer)
        Job.objects.create(
            employer=employer,
            company=company,
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
            positions=positions,
            requirements=requirements,
            is_featured=is_featured,
        )
        return redirect(reverse_lazy("home"))
    return render(request, "jobs/post-new-job.html")
