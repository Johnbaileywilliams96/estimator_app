from django.db import models
from .business_member import BusinessMember
from .project import Project



class ProjectEmployee(models.Model):
    business_member_id = models.ForeignKey(BusinessMember, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='employees')

