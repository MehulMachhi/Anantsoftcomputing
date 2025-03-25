from rest_framework import serializers
from .models import (
    Department, JobLocation, Skill, JobPosting,
    EmployeeTestimonial, BenefitCategory, JobApplication
)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id', 'name', 'slug', 'description', 'icon',
            'display_order', 'is_active', 'created_at'
        ]

class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = ['id', 'city', 'state', 'country', 'is_remote']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'slug', 'is_active']

class JobPostingSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    location = JobLocationSerializer(read_only=True)
    required_skills = SkillSerializer(many=True, read_only=True)
    preferred_skills = SkillSerializer(many=True, read_only=True)
    experience_range = serializers.CharField(source='get_experience_range', read_only=True)
    salary_range = serializers.CharField(source='get_salary_range', read_only=True)

    class Meta:
        model = JobPosting
        fields = [
            'id', 'title', 'slug', 'department', 'job_type',
            'experience_level', 'experience_years_min', 'experience_years_max',
            'experience_range', 'location', 'salary_min', 'salary_max',
            'salary_range', 'salary_is_visible', 'summary', 'description',
            'responsibilities', 'requirements', 'benefits',
            'required_skills', 'preferred_skills', 'is_featured',
            'is_urgent', 'status', 'applications_email', 'posting_date',
            'closing_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class EmployeeTestimonialSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = EmployeeTestimonial
        fields = [
            'id', 'name', 'role', 'department', 'quote',
            'image', 'is_featured', 'display_order',
            'is_active', 'created_at'
        ]

class BenefitCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitCategory
        fields = [
            'id', 'name', 'icon', 'description',
            'display_order', 'is_active'
        ]
        
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"