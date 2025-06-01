from django.db import models
from django.contrib.auth.models import User
from .business import Business

class BusinessMember(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    purchased_seats = models.IntegerField(default=1)

