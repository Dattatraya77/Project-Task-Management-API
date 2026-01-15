
from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]