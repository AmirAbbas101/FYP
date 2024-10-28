from django.shortcuts import render


# Create your views here.
def browseJobsView(request):
    employment_options = [
        {"id": "full-time", "value": "full-time", "label": "Full-time (3)"},
        {"id": "part-time", "value": "part-time", "label": "Part-time (5)"},
        # More options...
    ]
    context = {
        "employment_options": employment_options,
        # Additional context...
    }

    return render(request, "jobs/browse-jobs.html", context)
    