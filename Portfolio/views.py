from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProjectCategory, Technology, Project, ProjectImage
from .serializers import (
    ProjectCategorySerializer,
    TechnologySerializer,
    ProjectSerializer,
    ProjectImageSerializer
)

class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['display_order', 'name', 'created_at']
    ordering = ['display_order', 'name']

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'technologies', 'is_active', 'is_featured']
    search_fields = ['title', 'description', 'detailed_description', 'client']
    ordering_fields = ['display_order', 'created_at', 'completion_date']
    ordering = ['-is_featured', 'display_order', '-created_at']

    @action(detail=True, methods=['post'])
    def toggle_featured(self, request, pk=None):
        project = self.get_object()
        project.is_featured = not project.is_featured
        project.save()
        return Response({
            'status': 'success',
            'is_featured': project.is_featured
        })

    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        project = self.get_object()
        project.is_active = not project.is_active
        project.save()
        return Response({
            'status': 'success',
            'is_active': project.is_active
        })

    @action(detail=True)
    def images(self, request, pk=None):
        project = self.get_object()
        images = project.images.all()
        serializer = ProjectImageSerializer(images, many=True)
        return Response(serializer.data)

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['project', 'is_primary']
    ordering_fields = ['display_order', 'created_at']
    ordering = ['display_order']

    @action(detail=True, methods=['post'])
    def set_primary(self, request, pk=None):
        image = self.get_object()
        # Remove primary status from other images of this project
        image.project.images.filter(is_primary=True).update(is_primary=False)
        image.is_primary = True
        image.save()
        return Response({'status': 'success'})