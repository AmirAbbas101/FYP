from django.shortcuts import render


def home_view(request):
    companies = ["intel", "intel", "intel", "intel"]
    return render(request, "home.html", {"companies": companies})


def about_view(request):
    return render(request, "about.html")
