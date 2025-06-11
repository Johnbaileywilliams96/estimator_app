from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from backendapi.models.unit_of_measure import UnitOfMeasure
from backendapi.serializers.unit_of_measure_serializer import UnitOfMeasureSerializer
from rest_framework.response import Response



class UnitOfMeasureViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    

    def retrieve(self, request, pk):

        unit_of_measure = UnitOfMeasure.objects.get(pk=pk)

        serializer = UnitOfMeasureSerializer(
            unit_of_measure, many=False, context={"request": request}
        )
        return Response(serializer.data)

    def list(self, request):
        """Handle GET /unit_of_measure/ - return all unit_of_measure items"""
        measures = UnitOfMeasure.objects.all()
        serializer = UnitOfMeasureSerializer(
            measures, many=True, context={"request": request}
        )
        return Response(serializer.data)
    

    def create(self, request):
        unit_of_measure = UnitOfMeasure()
        unit_of_measure.unit_of_measure_id = request.data["unit_of_measure_id"]
        unit_of_measure.name = request.data["name"]
        unit_of_measure.abbreviation = request.data["abbreviation"]
        unit_of_measure.abbreviation = request.data["abbreviation"]
        
        unit_of_measure.save()

        serializer = UnitOfMeasureSerializer(
            unit_of_measure, many=False, context={"request": request}  # Change to many=False
        )
        return Response(serializer.data)


