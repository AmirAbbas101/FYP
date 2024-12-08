# from django.contrib import admin
# from .models import Candidate, User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [
#         "user_id",
#         "first_name",
#         "last_name",
#         "username",
#         "email",
#         "role",
#         "profile_img",
#         "date_joined",
#         "last_login",
#         "is_active",
#         "is_verified",
#         "password",
#     ]


# admin.site.register(Candidate)
# @admin.register(Candidate)
# class CandidateAdmin(admin.ModelAdmin):
#     list_display = [
#         "candidate_id",
#         "user",  # Display the related user (via ForeignKey or OneToOneField)
#     ]
#     search_fields = ["user__username", "user__email"]  # Enable search by user fields
#     list_filter = ["user__is_active", "user__role"]  # Filter by active status and role
