from django.shortcuts import render


def homeView(request):
    companies = ["intel", "intel", "intel", "intel"]
    return render(request, "home.html", {"companies": companies})


def aboutView(request):
    return render(request, "about.html")
