from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Testimonials, Portfolio, Aboutus
from .serializers import TestimonialsSerializer, PortfolioSerializer, AboutusSerializer

class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'designation', 'Company_Name']

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['Portfolio_category', 'Project_Techstack']
    search_fields = ['Project_title', 'Project_description']

class AboutusViewSet(viewsets.ModelViewSet):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]