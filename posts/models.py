from django.db import models
from django.contrib.auth import get_user_model

from core.models import UUIDModel


class Subject(UUIDModel):
    name = models.CharField(max_length=64, unique=True)


class Reason(UUIDModel):
    name = models.CharField(max_length=64, unique=True)


class Post(UUIDModel):
    subject = models.ManyToManyField(Subject, related_name='posts')
    reason = models.ManyToManyField(Reason, related_name='posts')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)