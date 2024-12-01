from django.shortcuts import render


def home_view(request):
    companies = ["intel", "intel", "intel", "intel"]
    page_name = "home"
    return render(request, "home.html", {"companies": companies, "page_name": page_name})


def about_view(request):
    return render(request, "about.html")
