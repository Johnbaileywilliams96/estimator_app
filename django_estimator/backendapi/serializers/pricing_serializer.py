from rest_framework import serializers
from backendapi.models.pricing import ItemPricing


class ItemPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPricing
        fields = [
            'id',
            'unit_of_measure_id',
            'labor_costs',
            'material',
            'margin_pct',
            'total_price'
        ]
        depth = 1
        
    def validate_labor_costs(self, value):
        """Ensure labor costs are not negative"""
        if value < 0:
            raise serializers.ValidationError("Labor costs cannot be negative")
        return value
    
    def validate_margin_pct(self, value):
        """Ensure margin percentage is between 0 and 100"""
        if value < 0 or value > 100:
            raise serializers.ValidationError("Margin percentage must be between 0 and 100")
        return value
    
    def validate_total_price(self, value):
        """Ensure total price is not negative"""
        if value < 0:
            raise serializers.ValidationError("Total price cannot be negative")
        return value