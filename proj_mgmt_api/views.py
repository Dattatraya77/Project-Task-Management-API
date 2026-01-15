from django.shortcuts import render
from .serializers import CompanySerializer, ProjectSerializer, TaskSerizlizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Company, Project, Task
from .permissions import IsAdmin, IsManagerOrIsAdmin, IsUserOrAbove


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all().order_by('-created_at')
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):

        user = self.request.user
        if not user.is_autheticated:
            return Project.objects.none()

        if user.profile.role in ["admin", "manager"]:
            return Project.objects.all().order_by('-created_at')

        return (
            Project.objects
            .filter(tasks__assigned_to=user)
            .distinct()
            .order_by('-created_at')
        )

    def get_permissions(self):
        if self.action in [
            "retrieve",
            "create",
            "update",
            "partial_update",
            "destroy"
        ]:
            return [IsAuthenticated(), IsManagerOrIsAdmin()]
        return [IsAuthenticated()]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.select_related("project", "assigned_to").order_by("-created_at")
    serializer_class = TaskSerizlizer
    permission_classes = [IsUserOrAbove]
