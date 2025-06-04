from rest_framework import serializers
from ..models import SubLibrary
from ..models import Library


class SubLibrarySerializer(serializers.ModelSerializer):
    library_name = serializers.CharField(source='library_id.name', read_only=True)
    
    class Meta:
        model = SubLibrary
        fields = ['id', 'library_id', 'library_name', 'name', 'description']
        depth = 1
        
    def validate_library_id(self, value):
        """
        Validate that the library exists and is accessible
        """
        if not isinstance(value, Library):
            raise serializers.ValidationError("Invalid library reference")
        return value

        