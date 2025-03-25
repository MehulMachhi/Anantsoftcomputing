# master/admin.py
from django.contrib import admin
from .models import ProjectTechstack, ProjectKeyFeature, PortfolioCategory, ProjectImpact

@admin.register(ProjectTechstack)
class ProjectTechstackAdmin(admin.ModelAdmin):
    list_display = ('name', 'truncated_description', 'has_icon', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)

    def truncated_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    truncated_description.short_description = 'Description'

    def has_icon(self, obj):
        return bool(obj.icon)
    has_icon.boolean = True
    has_icon.short_description = 'Has Icon'

@admin.register(ProjectKeyFeature)
class ProjectKeyFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'truncated_description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)

    def truncated_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    truncated_description.short_description = 'Description'

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'truncated_description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)

    def truncated_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    truncated_description.short_description = 'Description'

@admin.register(ProjectImpact)
class ProjectImpactAdmin(admin.ModelAdmin):
    list_display = ('title', 'truncated_description', 'truncated_metrics', 'created_at')
    search_fields = ('title', 'description', 'metrics')
    list_filter = ('created_at',)
    ordering = ('title',)

    def truncated_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    truncated_description.short_description = 'Description'

    def truncated_metrics(self, obj):
        return obj.metrics[:50] + '...' if len(obj.metrics) > 50 else obj.metrics
    truncated_metrics.short_description = 'Metrics'