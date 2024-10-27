from django.shortcuts import render


# Create your views here.
def browseJobsView(request):
    return render(request, "jobs/browse-jobs.html")
