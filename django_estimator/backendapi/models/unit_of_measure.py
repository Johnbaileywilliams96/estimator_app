from django.db import models


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "sq ft", "linear ft", "each", "hour"
    abbreviation = models.CharField(max_length=10, blank=True, null=True)  # e.g., "sqft", "lf", "ea", "hr"
    description = models.TextField(blank=True, null=True)

