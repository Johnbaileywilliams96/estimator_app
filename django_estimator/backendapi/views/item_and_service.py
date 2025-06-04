from rest_framework import viewsets
from backendapi.models.items_and_services import ItemsServices
from backendapi.serializers.item_and_service_serializer import ItemsServicesSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class ItemServicesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ItemsServices.objects.all()  # Add this line
    serializer_class = ItemsServicesSerializer
    