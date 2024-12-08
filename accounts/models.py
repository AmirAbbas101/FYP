from django.contrib.auth import get_user_model
from django.db import models
from accounts.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


class User(AbstractBaseUser):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=50, unique=True, verbose_name=_("Username"))
    email = models.EmailField(unique=True, verbose_name=_("Email Address"))
    password = models.CharField(max_length=255, verbose_name=_("Password"))
    role = models.CharField(
        max_length=50,
        choices=[("CA", "Candidate"), ("RE", "Recruiter")],
        default="CA",
        verbose_name=_("Role"),
    )
    profile_img = models.ImageField(
        default="profile_images/default.png",
        upload_to="profile_images",
        blank=True,
        null=True,
        verbose_name=_("Profile Image"),
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    last_login = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Last Login")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    is_verified = models.BooleanField(default=False, verbose_name=_("Verified"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Verified"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Verified"))

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.user_name

    def set_last_login(self):
        """
        Updates the last login time for the user.
        """
        self.last_login = timezone.now()
        self.save()

    def verify_user(self):
        """
        Marks the user as verified.
        """
        self.is_verified = True
        self.save()


class Candidate(models.Model):
    candidate_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="candidate_profile",
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
        verbose_name = _("candidate")
        verbose_name_plural = _("candidates")

    def __str__(self):
        return self.full_name

    def display_skills(self):
        """
        Returns a formatted string of skills as a list.
        """
        return [skill.strip() for skill in self.skills.split(",")]
