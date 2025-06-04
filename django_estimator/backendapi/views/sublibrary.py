from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import SubLibrary
from ..serializers import SubLibrarySerializer  # Adjust path as needed


class SublibraryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing SubLibrary instances
    Provides CRUD operations for SubLibraries with additional filtering
    """
    queryset = SubLibrary.objects.all()
    serializer_class = SubLibrarySerializer
    
    def get_queryset(self):
        """
        Filter sublibraries by library_id if provided as query parameter
        Usage: /api/sublibraries/?library_id=1
        """
        queryset = SubLibrary.objects.select_related('library_id').all()
        library_id = self.request.query_params.get('library_id', None)
        
        if library_id is not None:
            queryset = queryset.filter(library_id=library_id)
            
        return queryset.order_by('name')
    
    def create(self, request, *args, **kwargs):
        """
        Create a new SubLibrary instance
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
    
    def update(self, request, *args, **kwargs):
        """
        Update a SubLibrary instance
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete a SubLibrary instance
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['get'])
    def by_library(self, request):
        """
        Get all sublibraries grouped by library
        Usage: /api/sublibraries/by_library/
        """
        sublibraries = SubLibrary.objects.select_related('library_id').all()
        grouped_data = {}
        
        for sublibrary in sublibraries:
            library_name = sublibrary.library_id.name
            if library_name not in grouped_data:
                grouped_data[library_name] = []
            
            grouped_data[library_name].append({
                'id': sublibrary.id,
                'name': sublibrary.name,
                'description': sublibrary.description
            })
        
        return Response(grouped_data)
    
    @action(detail=True, methods=['get'])
    def library_info(self, request, pk=None):
        """
        Get detailed library information for a specific sublibrary
        Usage: /api/sublibraries/{id}/library_info/
        """
        sublibrary = self.get_object()
        library = sublibrary.library_id
        
        return Response({
            'sublibrary': {
                'id': sublibrary.id,
                'name': sublibrary.name,
                'description': sublibrary.description
            },
            'library': {
                'id': library.id,
                'name': library.name,
                # Add other library fields as needed
            }
        })

        