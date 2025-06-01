from django.db import models
from .project import Project

class ProjectFiles(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file_path = models.FileField(upload_to='project_files/')
    created_at = models.DateTimeField(auto_now_add=True)

