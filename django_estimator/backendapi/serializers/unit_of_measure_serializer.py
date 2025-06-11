from rest_framework import serializers
from backendapi.models.unit_of_measure import UnitOfMeasure


class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasure
        fields = [
            'id',
            'name',
            'abbreviation',
            'description'
            
        ]
        depth = 1
        







# from django.db import models


# # class UnitOfMeasure(models.Model):
# #     name = models.CharField(max_length=50, unique=True)  # e.g., "sq ft", "linear ft", "each", "hour"
# #     abbreviation = models.CharField(max_length=10, blank=True, null=True)  # e.g., "sqft", "lf", "ea", "hr"
# #     description = models.TextField(blank=True, null=True)

