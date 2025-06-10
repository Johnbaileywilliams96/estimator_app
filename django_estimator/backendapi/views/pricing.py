from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from backendapi.models.pricing import ItemPricing
from backendapi.serializers.pricing_serializer import ItemPricingSerializer
from rest_framework.response import Response



class ItemPricingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    

    def retrieve(self, request, pk):

        pricing = ItemPricing.objects.get(pk=pk)

        serializer = ItemPricingSerializer(
            pricing, many=False, context={"request": request}
        )
        return Response(serializer.data)

    def list(self, request):
        """Handle GET /pricing/ - return all pricing items"""
        pricing_items = ItemPricing.objects.all()
        serializer = ItemPricingSerializer(
            pricing_items, many=True, context={"request": request}
        )
        return Response(serializer.data)
    

    def create(self, request):
        pricing = ItemPricing()
        pricing.unit_of_measure_id = request.data["unit_of_measure_id"]
        pricing.labor_costs = request.data["labor_costs"]
        pricing.material = request.data["material"]
        pricing.margin_pct = request.data["margin_pct"]
        pricing.total_price = request.data["total_price"]
        
        pricing.save()

        serializer = ItemPricingSerializer(
            pricing, many=False, context={"request": request}  # Change to many=False
        )
        return Response(serializer.data)


