from rest_framework import serializers
from backendapi.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'client_id',
            'description',
            'status_id',
            'total_est',
            'business_type_id',
            'created_by'
        ]
        
    def validate_title(self, value):
        """Ensure title is not empty and has reasonable length"""
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        return value.strip()
    
    def validate_total_est(self, value):
        """Ensure total estimate is not negative if provided"""
        if value is not None and value < 0:
            raise serializers.ValidationError("Total estimate cannot be negative")
        return value
    
    def validate(self, data):
        """Cross-field validation"""
        # Ensure client_id is provided
        if not data.get('client_id'):
            raise serializers.ValidationError("Client is required")
        
        # Ensure created_by is provided
        if not data.get('created_by'):
            raise serializers.ValidationError("Created by field is required")
            
        return data