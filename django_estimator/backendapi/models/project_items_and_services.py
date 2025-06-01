from decimal import Decimal
from django.db import models
from .project import Project
from .items_and_services import ItemsServices

class ProjectItemsServices(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_items')
    items_id = models.ForeignKey(ItemsServices, on_delete=models.CASCADE)
    material_costs = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    labor_costs = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    unit_of_measure = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

 