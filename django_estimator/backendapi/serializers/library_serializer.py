from rest_framework import serializers
from backendapi.models.library import Library

class LibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Library  
        fields = [
            'id',
            'name',
            'description',
        ]
        read_only_fields = ['id']

        