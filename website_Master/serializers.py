from rest_framework import serializers
from .models import ProjectTechstack, ProjectKeyFeature, PortfolioCategory, ProjectImpact

class ProjectTechstackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechstack
        fields = ['id', 'name', 'description', 'icon', 'created_at']

class ProjectKeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectKeyFeature
        fields = ['id', 'name', 'description', 'created_at']

class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ['id', 'name', 'description', 'created_at']

class ProjectImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImpact
        fields = ['id', 'title', 'description', 'metrics', 'created_at']