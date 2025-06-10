from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from backendapi.models.client import Client
from backendapi.serializers.clients_serializer import ClientSerializer
from rest_framework.response import Response

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
  

    def list(self, request):

        clients = Client.objects.all()

        serializer = ClientSerializer(
            clients, many=True, context={"request": request}
        )
        return Response(serializer.data)


