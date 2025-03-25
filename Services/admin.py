# services/admin.py
from django.contrib import admin
from .models import Service, ServiceCategory, ServiceFeature, ServiceImage

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'icon', 'is_active', 'display_order', 'created_at')
    list_filter = ('is_active', 'category', 'gradient')
    search_fields = ('title', 'description', 'detailed_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline, ServiceImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Appearance', {
            'fields': ('icon', 'gradient', 'display_order', 'is_active')
        }),
        ('Detailed Information', {
            'fields': ('detailed_description', 'features', 'benefits'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('display_order', 'title')

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'display_order')
    list_filter = ('service',)
    search_fields = ('title', 'description')
    ordering = ('service', 'display_order')

@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('service', 'alt_text', 'is_primary', 'display_order')
    list_filter = ('service', 'is_primary')
    search_fields = ('alt_text',)
    ordering = ('service', 'display_order')