from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):
    business_phone = models.CharField(max_length=20, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_name = models.CharField(max_length=200)
    creator_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    business_preset_type_id = models.IntegerField(blank=True, null=True)
    joinable = models.BooleanField(default=True)
    seats = models.IntegerField(default=1)
