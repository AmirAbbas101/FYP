from django.urls import path

from . import views

urlpatterns = [
    path("", views.browseJobsView, name="browse-jobs")
]