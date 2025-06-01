from django.db import models


class BusinessPresetType(models.Model):
    name = models.CharField(max_length=100)


