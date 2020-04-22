from django.db import models


class Url(models.Model):
    title = models.CharField(max_length=128, blank=False)
    reference = models.CharField(max_length=256, blank=False)
    description = models.TextField()
    usable = models.BooleanField(default=False)
    checking_now = models.BooleanField(default=False)