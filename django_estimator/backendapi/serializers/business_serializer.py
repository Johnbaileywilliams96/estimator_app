from rest_framework import serializers
from backendapi.models.business import Business


class BusinessSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Business
        fields = [
            'id',
            'business_phone',
            'business_email',
            'business_name',
            'creator_id',
            'business_preset_type_id',
            'joinable',
            
        ]
        depth = 1
