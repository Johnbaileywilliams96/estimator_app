from rest_framework import viewsets
from backendapi.models.library import Library
from backendapi.serializers.library_serializer import LibrarySerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class LibraryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Library.objects.all()  # Add this line
    serializer_class = LibrarySerializer
    
    def list(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(
            libraries, many=True, context={'request': request}
        )
        return Response(serializer.data)