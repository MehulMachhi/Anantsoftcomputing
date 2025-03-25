from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Department, JobLocation, Skill, JobPosting,
    EmployeeTestimonial, BenefitCategory, JobApplication
)
from .serializers import (
    DepartmentSerializer, JobLocationSerializer, SkillSerializer,
    JobPostingSerializer, EmployeeTestimonialSerializer,
    BenefitCategorySerializer, JobApplicationSerializer
)
from rest_framework import generics

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['display_order', 'name']
    ordering = ['display_order', 'name']

class JobLocationViewSet(viewsets.ModelViewSet):
    queryset = JobLocation.objects.all()
    serializer_class = JobLocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country', 'state', 'is_remote']
    search_fields = ['city', 'state', 'country']

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_active']
    search_fields = ['name']

class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        'department', 'job_type', 'experience_level', 'location',
        'status', 'is_featured', 'is_urgent'
    ]
    search_fields = [
        'title', 'summary', 'description', 'responsibilities',
        'requirements', 'benefits'
    ]
    ordering_fields = ['posting_date', 'created_at', 'display_order']
    ordering = ['-is_featured', '-posting_date']

    @action(detail=True, methods=['post'])
    def toggle_featured(self, request, pk=None):
        job = self.get_object()
        job.is_featured = not job.is_featured
        job.save()
        return Response({'status': 'success', 'is_featured': job.is_featured})

    @action(detail=True, methods=['post'])
    def toggle_urgent(self, request, pk=None):
        job = self.get_object()
        job.is_urgent = not job.is_urgent
        job.save()
        return Response({'status': 'success', 'is_urgent': job.is_urgent})

class EmployeeTestimonialViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTestimonial.objects.filter(is_active=True)
    serializer_class = EmployeeTestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'is_featured']
    search_fields = ['name', 'role', 'quote']
    ordering_fields = ['display_order', 'created_at']
    ordering = ['-is_featured', 'display_order']

    @action(detail=True, methods=['post'])
    def toggle_featured(self, request, pk=None):
        testimonial = self.get_object()
        testimonial.is_featured = not testimonial.is_featured
        testimonial.save()
        return Response({'status': 'success', 'is_featured': testimonial.is_featured})

class BenefitCategoryViewSet(viewsets.ModelViewSet):
    queryset = BenefitCategory.objects.filter(is_active=True)
    serializer_class = BenefitCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['display_order']
    ordering = ['display_order']
    
class JobApplicationView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer