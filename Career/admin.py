# careers/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Department , JobLocation , Skill , JobPosting ,
    EmployeeTestimonial , BenefitCategory, JobApplication
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' , 'is_active' , 'display_order')
    prepopulated_fields = {'slug': ('name' ,)}
    list_filter = ('is_active' ,)
    search_fields = ('name' , 'description')
    ordering = ('display_order' , 'name')


@admin.register(JobLocation)
class JobLocationAdmin(admin.ModelAdmin):
    list_display = ('city' , 'state' , 'country' , 'is_remote')
    list_filter = ('country' , 'state' , 'is_remote')
    search_fields = ('city' , 'state' , 'country')
    ordering = ('country' , 'state' , 'city')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' , 'is_active')
    prepopulated_fields = {'slug': ('name' ,)}
    list_filter = ('is_active' ,)
    search_fields = ('name' ,)
    ordering = ('name' ,)
    
class JobApplicationInline(admin.TabularInline): 
    model = JobApplication
    extra = 1  
    fields = ['name', 'phone', 'email', 'address', 'years_of_experience', 'resume']


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        'title' , 'department' , 'location' , 'job_type' ,
        'experience_range' , 'status' , 'is_featured' , 'is_urgent'
    )
    list_filter = (
        'status' , 'job_type' , 'department' , 'location' ,
        'is_featured' , 'is_urgent'
    )
    search_fields = ('title' , 'summary' , 'description')
    prepopulated_fields = {'slug': ('title' ,)}
    filter_horizontal = ('required_skills' , 'preferred_skills')
    inlines = [JobApplicationInline]

    fieldsets = (
        ('Basic Information' , {
            'fields': (
                'title' , 'slug' , 'department' , 'job_type' ,
                'experience_level' , 'experience_years_min' , 'experience_years_max'
            )
        }) ,
        ('Location & Salary' , {
            'fields': (
                'location' , 'salary_min' , 'salary_max' , 'salary_is_visible'
            )
        }) ,
        ('Job Details' , {
            'fields': (
                'summary' , 'description' , 'responsibilities' ,
                'requirements' , 'benefits'
            )
        }) ,
        ('Skills' , {
            'fields': ('required_skills' , 'preferred_skills')
        }) ,
        ('Publishing' , {
            'fields': (
                'status' , 'is_featured' , 'is_urgent' ,
                'posting_date' , 'closing_date' , 'applications_email'
            )
        }) ,
    )

    def experience_range(self , obj):
        return obj.get_experience_range()

    experience_range.short_description = 'Experience'


@admin.register(EmployeeTestimonial)
class EmployeeTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name' , 'role' , 'department' , 'is_featured' , 'is_active' , 'thumbnail')
    list_filter = ('is_featured' , 'is_active' , 'department')
    search_fields = ('name' , 'role' , 'quote')
    ordering = ('-is_featured' , 'display_order')

    def thumbnail(self , obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>' ,
                obj.image.url
            )
        return "No Image"

    thumbnail.short_description = 'Photo'


@admin.register(BenefitCategory)
class BenefitCategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'icon' , 'is_active' , 'display_order')
    list_filter = ('is_active' ,)
    search_fields = ('name' , 'description')
    ordering = ('display_order' ,)
    
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'years_of_experience',)
    list_filter = ('years_of_experience',)
    search_fields = ('name', 'years_of_experience',)