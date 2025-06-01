from django.db import models
from .business import Business

class BusinessFiles(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='files')
    file_path = models.FileField(upload_to='business_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    field = models.CharField(max_length=100, blank=True, null=True)


 

