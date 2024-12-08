from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Candidate(models.Model):
    candidate_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="candidate_profile_userpanel",
        verbose_name=_("User"),
    )
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"))
    phone = models.CharField(
        max_length=15,
        verbose_name=_("Phone Number"),
        help_text=_("Enter a valid phone number."),
    )
    address = models.TextField(verbose_name=_("Address"))
    skills = models.TextField(
        verbose_name=_("Skills"),
        help_text=_("List skills separated by commas, e.g., Python, Django, React."),
    )
    education = models.TextField(
        verbose_name=_("Education"),
        help_text=_(
            "Provide educational background with degrees, institutions, and years."
        ),
    )
    experience = models.TextField(
        verbose_name=_("Experience"),
        help_text=_(
            "List previous work experience with roles, companies, and durations."
        ),
    )
    resume_file = models.FileField(
        upload_to="resumes/",
        verbose_name=_("Resume File"),
        help_text=_("Upload your resume in PDF format."),
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Profile Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Profile Updated At")
    )

    class Meta:
        ordering = ["full_name"]
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")

    def __str__(self):
        return self.full_name

    def display_skills(self):
        """
        Returns a formatted string of skills as a list.
        """
        return [skill.strip() for skill in self.skills.split(",")]
