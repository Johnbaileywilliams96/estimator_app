from rest_framework import serializers
from ..models import ItemsServices


class ItemsServicesSerializer(serializers.ModelSerializer):
    sub_library_name = serializers.CharField(source='sub_library_id.name', read_only=True)
    library_name = serializers.CharField(source='sub_library_id.library.name', read_only=True)
    library_id = serializers.IntegerField(source='sub_library_id.library.id', read_only=True)
    
    class Meta:
        model = ItemsServices
        fields = [
            'id',
            'name',
            'sub_library_id',
            'sub_library_name',
            'library_id',
            'library_name',
            'description',
            'item_pricing_id'
        ]
        depth = 1
