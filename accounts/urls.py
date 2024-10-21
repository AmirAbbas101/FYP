from django.urls import path
from accounts.views import registerView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.registerView, name="register"),
]
