from django.db import models
from accounts.manager import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    class Role(models.TextChoices):
        CANDIDATE = "CA", "Candidate"
        RECRUITER = "RE", "Recruiter"

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        max_length=50, blank=False, help_text='Enter your first name', null=False
    )  # Optional first name
    last_name = models.CharField(
        max_length=50, blank=False, help_text='Enter your last name', null=False
    )  # Optional last name
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    profile_img = models.ImageField(
        default="profile_pics/default.png", upload_to="profile_pics"
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.CANDIDATE)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.username
        
    
class CandiddateModel(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='candidat_profile')
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skills = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/',blank=True, null=True)  

    class Meta:
        verbose_name = 'Candidate'
        verbose_name_plural= 'Candidates'
    
    def __str__(self):
        return f'Candidate: {self.user.username}'