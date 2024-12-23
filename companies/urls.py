from django.urls import path
from . import views

urlpatterns = [
    path("", views.company_dashboard_view, name="company-dashboard"),
    path("job-listing", views.job_listing_view, name="post-a-job"),
    path("post-job/", views.postJobView, name="post-job"),
    path(
        "settings/<int:company_id>/<str:company_name>/",
        views.settings_view,
        name="company-settings",
    ),
]
