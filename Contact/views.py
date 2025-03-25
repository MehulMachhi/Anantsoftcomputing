from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import ContactInformation, ServiceType, ContactEnquiry
from .serializers import (
    ContactInformationSerializer,
    ServiceTypeSerializer,
    ContactEnquirySerializer
)

class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Return only the first instance for GET requests
        if self.request.method == 'GET':
            return ContactInformation.objects.all()[:1]
        return ContactInformation.objects.all()

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.filter(is_active=True)
    serializer_class = ServiceTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering = ['name']

class ContactEnquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactEnquiry.objects.all()
    serializer_class = ContactEnquirySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'service']
    search_fields = ['name', 'email', 'company', 'message']
    ordering = ['-created_at']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return super().get_permissions()

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        enquiry = self.get_object()
        status = request.data.get('status')
        if status in dict(ContactEnquiry.STATUS_CHOICES):
            enquiry.status = status
            enquiry.save()
            return Response({
                'status': 'success',
                'current_status': status
            })
        return Response({
            'status': 'error',
            'message': 'Invalid status'
        }, status=status.HTTP_400_BAD_REQUEST)