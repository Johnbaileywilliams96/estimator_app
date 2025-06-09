from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from backendapi.models.business import Business
from backendapi.serializers.business_serializer import BusinessSerializer
from rest_framework.response import Response



class BusinessViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    

    def retrieve(self, request, pk):

        business = Business.objects.get(pk=pk)

        serializer = BusinessSerializer(
            business, many=False, context={"request": request}
        )
        return Response(serializer.data)
    

    def create(self, request):

        business = Business()
        business.creator_id = request.data["creator_id"]
        business.business_email = request.data["business_email"]
        business.business_name = request.data["business_name"]
        business.business_phone = request.data["business_phone"]
        business.business_preset_type_id = request.data["business_preset_type_id"]
        
        business.save()

        serializer = BusinessSerializer(
            business, many=True, context={"request": request}
        )
        return Response(serializer.data)


