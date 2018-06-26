import shortuuid

from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=shortuuid.uuid())

    class Meta:
        abstract = True