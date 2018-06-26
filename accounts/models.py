from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    location = models.CharField(max_length=128, blank=True, null=True)
    profile_photo = models.ImageField(blank=True, null=True)