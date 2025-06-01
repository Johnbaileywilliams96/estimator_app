from django.db import models
from .sublibrary import SubLibrary


class ItemsServices(models.Model):
    name = models.CharField(max_length=100)
    sub_library_id = models.ForeignKey(SubLibrary, on_delete=models.CASCADE, related_name='items_services')
    description = models.TextField(blank=True, null=True)
    item_pricing_id = models.IntegerField(blank=True, null=True)  # Reference to ItemPricing

