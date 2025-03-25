from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, Service, ServiceFeature, ServiceImage
from .serializers import (
    ServiceCategorySerializer,
    ServiceSerializer,
    ServiceFeatureSerializer,
    ServiceImageSerializer
)

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_active', 'gradient']
    search_fields = ['title', 'description', 'detailed_description']
    ordering_fields = ['display_order', 'title', 'created_at']
    ordering = ['display_order', 'title']

    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        service = self.get_object()
        service.is_active = not service.is_active
        service.save()
        return Response({
            'status': 'success',
            'is_active': service.is_active
        })

    @action(detail=True)
    def features(self, request, pk=None):
        service = self.get_object()
        features = service.feature_list.all()
        serializer = ServiceFeatureSerializer(features, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def images(self, request, pk=None):
        service = self.get_object()
        images = service.images.all()
        serializer = ServiceImageSerializer(images, many=True)
        return Response(serializer.data)

class ServiceFeatureViewSet(viewsets.ModelViewSet):
    queryset = ServiceFeature.objects.all()
    serializer_class = ServiceFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['service']
    search_fields = ['title', 'description']
    ordering_fields = ['display_order']
    ordering = ['display_order']

class ServiceImageViewSet(viewsets.ModelViewSet):
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['service', 'is_primary']
    ordering_fields = ['display_order']
    ordering = ['display_order']