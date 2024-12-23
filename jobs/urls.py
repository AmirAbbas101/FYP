from django.urls import path
from .views import JobListView, post_job_view, JobDetailView

urlpatterns = [
    path("", JobListView.as_view(), name="browse-jobs"),
    path(
        "<int:job_id>/<slug:job_title>/",
        JobDetailView,
        name="job-detail",
    ),
    path("post_job/<int:user_id>", post_job_view, name="post-job"),
]
