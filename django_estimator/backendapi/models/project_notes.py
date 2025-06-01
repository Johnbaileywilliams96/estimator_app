from django.db import models
from .business_member import BusinessMember
from .project import Project


class ProjectNotes(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(BusinessMember, on_delete=models.CASCADE)
 
 