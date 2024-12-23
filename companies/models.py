from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="employer_profile",
        verbose_name=_("User"),
    )
    company_name = models.CharField(max_length=255, verbose_name=_("Company Name"))
    company_website = models.URLField(
        max_length=255,
        verbose_name=_("Company Website"),
        blank=True,
        help_text=_("Provide the official company website URL."),
    )
    company_address = models.TextField(verbose_name=_("Company Address"))
    company_logo = models.ImageField(
        upload_to="company_logos/",
        verbose_name=_("Company Logo"),
        blank=True,
        null=True,
        help_text=_("Upload the company logo. (Optional)"),
    )
    contact_person = models.CharField(
        max_length=255,
        verbose_name=_("Contact Person"),
        help_text=_("Full name of the primary contact person."),
    )
    contact_email = models.EmailField(verbose_name=_("Contact Email"))
    contact_phone = models.CharField(
        max_length=15,
        verbose_name=_("Contact Phone Number"),
        blank=True,
        help_text=_("Optional contact phone number."),
    )
    industry = models.CharField(
        max_length=100,
        verbose_name=_("Industry"),
        help_text=_("e.g., IT, Healthcare, Manufacturing."),
    )
    company_size = models.CharField(
        max_length=50,
        verbose_name=_("Company Size"),
        help_text=_("e.g., 1-10, 11-50, 51-200 employees."),
    )
    description = models.TextField(
        verbose_name=_("Company Description"),
        blank=True,
        help_text=_("Optional detailed description of the company."),
    )
    established_year = models.PositiveIntegerField(
        verbose_name=_("Established Year"),
        blank=True,
        null=True,
        help_text=_("Year the company was established. (Optional)"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Profile Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Profile Updated At")
    )

    class Meta:
        ordering = ["company_name"]
        verbose_name = _("Employer")
        verbose_name_plural = _("Employers")

    def __str__(self):
        return self.company_name

    def get_full_contact_details(self):
        """
        Returns the contact person's full details.
        """
        return f"{self.contact_person} ({self.contact_email})"

    def is_new_company(self):
        """
        Checks if the company is recently established.
        """
        if self.established_year:
            current_year = timezone.now().year
            return current_year - self.established_year <= 5
        return False
