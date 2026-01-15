from .models import Company, Project, UserProfile, Task
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    company_name =serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class TaskSerizlizer(serializers.ModelSerializer):
    project_name = serializers.CharField(source="project.name", read_only=True)
    assigned_to = serializers.CharField(source="assigned_to.username", read_only=True)

    class Meta:
        model = Task
        fields = "__all__"