from rest_framework import serializers
from backendapi.models.client import Client
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'country',
            'phone',
            'email_address',
            'created_at',
            'created_by',
            'created_by_username',
            'references',
            'type_of_project',
            'notes',
            'status'
        ]
        read_only_fields = ['id', 'created_at', 'created_by_username']

