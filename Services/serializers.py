from rest_framework import serializers
from .models import ServiceCategory, Service, ServiceFeature, ServiceImage

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'description', 'created_at']

class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ['id', 'title', 'description', 'icon', 'display_order']

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id', 'image', 'alt_text', 'display_order', 'is_primary']

class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(),
        source='category',
        write_only=True
    )
    feature_list = ServiceFeatureSerializer(many=True, read_only=True)
    images = ServiceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'slug', 'description', 'icon', 'gradient',
            'category', 'category_id', 'detailed_description', 'features',
            'benefits', 'is_active', 'display_order', 'created_at',
            'updated_at', 'feature_list', 'images'
        ]