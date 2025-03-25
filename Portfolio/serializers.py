from rest_framework import serializers
from .models import ProjectCategory, Technology, Project, ProjectImage, Keyfeature

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = [
            'id', 'name', 'identifier', 'description',
            'display_order', 'is_active', 'created_at'
        ]

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'slug', 'description', 'created_at']

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = [
            'id', 'image', 'alt_text', 'display_order',
            'is_primary', 'created_at'
        ]
        
class KeyfeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyfeature
        fields = [
            'id', 'title'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProjectCategory.objects.all(),
        source='category',
        write_only=True
    )
    technologies = TechnologySerializer(many=True, read_only=True)
    technology_ids = serializers.PrimaryKeyRelatedField(
        queryset=Technology.objects.all(),
        source='technologies',
        write_only=True,
        many=True
    )
    images = ProjectImageSerializer(many=True, read_only=True)
    keyfeature = KeyfeatureSerializer(many=True, read_only=True, source='Key_feature')

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'category', 'category_id',
            'technologies', 'technology_ids', 'description',
            'detailed_description', 'featured_image', 'gradient',
            'live_url', 'repository_url', 'case_study_url',
            'client', 'duration', 'completion_date',
            'is_featured', 'display_order', 'is_active',
            'created_at', 'updated_at', 'images', 'keyfeature',
        ]