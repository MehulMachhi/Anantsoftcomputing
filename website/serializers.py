from rest_framework import serializers
from website_Master.serializers import (
    ProjectTechstackSerializer,
    ProjectKeyFeatureSerializer,
    PortfolioCategorySerializer,
    ProjectImpactSerializer
)
from .models import Testimonials, Portfolio, Aboutus

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    Portfolio_category = PortfolioCategorySerializer(read_only=True)
    Project_Techstack = ProjectTechstackSerializer(many=True, read_only=True)
    Project_KeyFeatures = ProjectKeyFeatureSerializer(many=True, read_only=True)
    Project_Impact = ProjectImpactSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = [
            'id', 'Portfolio_category', 'Project_title',
            'Project_Techstack', 'Project_KeyFeatures', 'Project_Impact',
            'Project_live_link', 'Project_Repos_link',
            'Project_case_study_link', 'Project_description', 'Project_image'
        ]

class AboutusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutus
        fields = ['id', 'Mission', 'Vision', 'aboutus_title', 'Core_values']