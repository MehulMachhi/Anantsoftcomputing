from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProjectTechstack, ProjectKeyFeature, PortfolioCategory, ProjectImpact
from .serializers import (
    ProjectTechstackSerializer,
    ProjectKeyFeatureSerializer,
    PortfolioCategorySerializer,
    ProjectImpactSerializer
)

class ProjectTechstackViewSet(viewsets.ModelViewSet):
    queryset = ProjectTechstack.objects.all()
    serializer_class = ProjectTechstackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class ProjectKeyFeatureViewSet(viewsets.ModelViewSet):
    queryset = ProjectKeyFeature.objects.all()
    serializer_class = ProjectKeyFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class PortfolioCategoryViewSet(viewsets.ModelViewSet):
    queryset = PortfolioCategory.objects.all()
    serializer_class = PortfolioCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class ProjectImpactViewSet(viewsets.ModelViewSet):
    queryset = ProjectImpact.objects.all()
    serializer_class = ProjectImpactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'metrics']
    ordering_fields = ['title', 'created_at']
    ordering = ['title']