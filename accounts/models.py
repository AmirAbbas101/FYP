from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        CANDIDATE = "CA", "Candidate"
        RECRUITER = "RE", "Recruiter"


    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)  # Allow first name to be optional
    last_name = models.CharField(max_length=50, blank=True, null=True)   # Allow last name to be optional
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    profile_img = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.CANDIDATE)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
