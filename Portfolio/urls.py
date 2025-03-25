from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectCategoryViewSet,
    TechnologyViewSet,
    ProjectViewSet,
    ProjectImageViewSet
)

router = DefaultRouter()
router.register('categories', ProjectCategoryViewSet, basename='project-categories')
router.register('technologies', TechnologyViewSet, basename='technologies')
router.register('projects', ProjectViewSet, basename='projects')
router.register('images', ProjectImageViewSet, basename='project-images')

urlpatterns = [
    path('', include(router.urls)),
]