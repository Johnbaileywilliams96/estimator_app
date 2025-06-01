from decimal import Decimal
from django.db import models


class ItemPricing(models.Model):
    unit_of_measure_id = models.CharField(max_length=50)  # This seems to reference unit_of_measure
    labor_costs = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    material = models.CharField(max_length=100, blank=True, null=True)
    margin_pct = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Pricing for {self.material or 'Item'}"

    class Meta:
        db_table = 'item_pricing'