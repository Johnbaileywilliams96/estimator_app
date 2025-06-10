from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from backendapi.models.project import Project
from backendapi.serializers.project_serializer import ProjectSerializer
from rest_framework.response import Response



class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    

    def retrieve(self, request, pk):

        project = Project.objects.get(pk=pk)

        serializer = ProjectSerializer(
            project, many=False, context={"request": request}
        )
        return Response(serializer.data)

    def list(self, request):
        """Handle GET /project/ - return all project items"""
        projects = Project.objects.all()
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request}
        )
        return Response(serializer.data)
    

    def create(self, request):
        project = Project()
        project.title = request.data["title"]
        project.client_id = request.data["client_id"]
        project.description = request.data["description"]
        project.status_id = request.data["status_id"]
        project.total_est = request.data["total_est"]
        project.business_type_id = request.data["business_type_id"]
        project.created_by = request.data["created_by"]
        project.save()

        serializer = ProjectSerializer(
            project, many=False, context={"request": request}  # Change to many=False
        )
        return Response(serializer.data)


