from django.db import models
from .library import Library

class SubLibrary(models.Model):
    library_id = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='sub_libraries')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

