from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("FT", "Full-Time"),
        ("PT", "Part-Time"),
        ("CT", "Contract"),
        ("IN", "Internship"),
        ("FR", "Freelance"),
    ]

    EXPERIENCE_LEVEL_CHOICES = [
        ("EN", "Entry-Level"),
        ("MI", "Mid-Level"),
        ("SE", "Senior-Level"),
    ]

    STATUS_CHOICES = [
        ("OP", "Open"),
        ("CL", "Closed"),
        ("DR", "Draft"),
    ]

    job_id = models.BigAutoField(primary_key=True)
    employer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="jobs",
        verbose_name=_("Employer"),
    )
    job_title = models.CharField(max_length=255, verbose_name=_("Job Title"))
    job_description = models.TextField(verbose_name=_("Job Description"))
    job_type = models.CharField(
        max_length=2, choices=JOB_TYPE_CHOICES, verbose_name=_("Job Type")
    )
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    salary_range = models.CharField(
        max_length=50,
        verbose_name=_("Salary Range"),
        help_text=_('Specify the range as "min-max" (e.g., 50k-80k)'),
    )
    experience_level = models.CharField(
        max_length=2,
        choices=EXPERIENCE_LEVEL_CHOICES,
        verbose_name=_("Experience Level"),
    )
    skills_required = models.TextField(verbose_name=_("Skills Required"))
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Posted"))
    application_deadline = models.DateField(verbose_name=_("Application Deadline"))
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default="OP", verbose_name=_("Status")
    )
    job_category = models.CharField(max_length=100, verbose_name=_("Job Category"))
    responsibilities = models.TextField(verbose_name=_("Responsibilities"))
    is_featured = models.BooleanField(default=False, verbose_name=_("Featured Job"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        ordering = ["-date_posted"]
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return f"{self.job_title} - {self.location}"


class Application(models.Model):
    STATUS_CHOICES = [
        ("PEN", "Pending"),
        ("REV", "Under Review"),
        ("APP", "Approved"),
        ("REJ", "Rejected"),
    ]

    application_id = models.BigAutoField(primary_key=True)
    job = models.ForeignKey(
        "Job",
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name=_("Job"),
    )
    job_seeker = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name=_("Job Seeker"),
    )
    resume_file = models.FileField(
        upload_to="resumes/",
        verbose_name=_("Resume File"),
        help_text=_("Upload your resume in PDF format."),
    )
    cover_letter = models.TextField(
        verbose_name=_("Cover Letter"),
        blank=True,
        help_text=_("Optional cover letter for your application."),
    )
    application_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Application Date")
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default="PEN",
        verbose_name=_("Application Status"),
    )
    reviewed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Reviewed At"),
        help_text=_("Timestamp when the application was reviewed."),
    )

    class Meta:
        ordering = ["-application_date"]
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        unique_together = (
            "job",
            "job_seeker",
        )  # Prevent duplicate applications for the same job by the same user.

    def __str__(self):
        return f"Application #{self.application_id} by {self.job_seeker} for {self.job}"

    def mark_reviewed(self, status):
        """
        Marks the application as reviewed with a specific status.
        """
        self.status = status
        self.reviewed_at = timezone.now()
        self.save()
