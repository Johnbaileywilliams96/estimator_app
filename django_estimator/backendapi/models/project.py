from django.db import models
from .client import Client
from .status import Status
from .business_type import BusinessPresetType
from .business_member import BusinessMember

class Project(models.Model):
    title = models.CharField(max_length=200)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField(blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    total_est = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    business_type_id = models.ForeignKey(BusinessPresetType, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(BusinessMember, on_delete=models.CASCADE)

   