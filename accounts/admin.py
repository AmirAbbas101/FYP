from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "username",
        "email",
        "role",
        "profile_img",
        "date_joined",
        "last_login",
        "is_active",
        "is_verified",
        "password",
    ]
