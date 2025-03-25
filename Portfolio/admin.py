# portfolio/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import ProjectCategory , Technology , Project , ProjectImage, Keyfeature


class KeyfeatureInline(admin.TabularInline):
    model = Keyfeature
    extra = 1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image' , 'alt_text' , 'display_order' , 'is_primary')


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'identifier' , 'display_order' , 'is_active' , 'created_at')
    list_filter = ('is_active' ,)
    search_fields = ('name' , 'identifier' , 'description')
    prepopulated_fields = {'identifier': ('name' ,)}
    ordering = ('display_order' , 'name')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name' , 'created_at')
    search_fields = ('name' , 'description')
    prepopulated_fields = {'slug': ('name' ,)}
    ordering = ('name' ,)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title' , 'category' , 'display_tech_stack' , 'is_featured' , 'is_active' , 'created_at')
    list_filter = ('is_active' , 'is_featured' , 'category' , 'technologies')
    search_fields = ('title' , 'description' , 'detailed_description')
    prepopulated_fields = {'slug': ('title' ,)}
    filter_horizontal = ('technologies' ,)
    inlines = [ProjectImageInline, KeyfeatureInline]

    fieldsets = (
        (None , {
            'fields': ('title' , 'slug' , 'category' , 'technologies' , 'description')
        }) ,
        ('Visual Elements' , {
            'fields': ('featured_image' , 'gradient')
        }) ,
        ('Project Links' , {
            'fields': ('live_url' , 'repository_url' , 'case_study_url')
        }) ,
        ('Project Details' , {
            'fields': ('client' , 'duration' , 'completion_date' , 'detailed_description',)
        }) ,
        ('Display Options' , {
            'fields': ('is_featured' , 'display_order' , 'is_active')
        }) ,
    )

    def display_tech_stack(self , obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])

    display_tech_stack.short_description = 'Technologies'


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail' , 'project' , 'alt_text' , 'display_order' , 'is_primary')
    list_filter = ('project' , 'is_primary')
    search_fields = ('project__title' , 'alt_text')
    ordering = ('project' , 'display_order')

    def thumbnail(self , obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>' , obj.image.url)
        return "No Image"

    thumbnail.short_description = 'Image Preview'