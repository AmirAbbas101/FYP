from django.contrib.auth import get_user_model
from django.db import models
from accounts.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid
from django.utils.timezone import now, timedelta


class User(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, verbose_name=_("Username"))
    email = models.EmailField(unique=True, verbose_name=_("Email Address"))
    password = models.CharField(max_length=255, verbose_name=_("Password"))
    role = models.CharField(
        max_length=50,
        choices=[("CA", "Candidate"), ("RE", "Recruiter")],
        default="CA",
        verbose_name=_("Role"),
    )
    profile_img = models.ImageField(
        default="profile_images/default.png", upload_to="profile_images"
    )

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    last_login = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Last Login")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))
    is_verified = models.BooleanField(default=False, verbose_name=_("Verified"))
    date_verified = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Date Verified")
    )
    is_staff = models.BooleanField(default=False, verbose_name=_("Verified"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Verified"))

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

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

    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        """
        return self.is_superuser or self.is_staff

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        """
        return self.is_superuser or self.is_staff


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    @property
    def is_expired(self):
        expiration_time = self.created_when + timedelta(minutes=10)
        return now() > expiration_time

    def __str__(self):
        return f"Password reset for {self.user.email}"


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
