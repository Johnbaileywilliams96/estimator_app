from django.db import models
from .client import Client

class Standing(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='standing')
    name = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Standing for {self.client}"

    class Meta:
        db_table = 'standing'