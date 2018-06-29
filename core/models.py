import shortuuid

from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=shortuuid.uuid())

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateField(auto_now=True)

    class Meta:
        abstract = True