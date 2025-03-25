# website/admin.py
from django.contrib import admin
from website.models import Testimonials , Portfolio , Aboutus


# Register Testimonials
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name' , 'designation' , 'Company_Name')
    search_fields = ('name' , 'designation' , 'Company_Name' , 'content')
    list_filter = ('designation' , 'Company_Name')
    ordering = ('name' ,)


# Register Portfolio
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('Project_title' , 'Portfolio_category' , 'get_techstack' , 'Project_live_link')
    search_fields = ('Project_title' , 'Project_description' , 'Portfolio_category__name')
    list_filter = ('Portfolio_category' , 'Project_Techstack')
    filter_horizontal = ('Project_Techstack' , 'Project_KeyFeatures')
    raw_id_fields = ('Portfolio_category' , 'Project_Impact')

    def get_techstack(self , obj):
        return ", ".join([tech.name for tech in obj.Project_Techstack.all()])

    get_techstack.short_description = 'Tech Stack'


# Register Aboutus
@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('aboutus_title' , 'truncated_mission' , 'truncated_vision' , 'truncated_core_values')
    search_fields = ('aboutus_title' , 'Mission' , 'Vision' , 'Core_values')

    def truncated_mission(self , obj):
        return obj.Mission[:50] + '...' if len(obj.Mission) > 50 else obj.Mission

    truncated_mission.short_description = 'Mission'

    def truncated_vision(self , obj):
        return obj.Vision[:50] + '...' if len(obj.Vision) > 50 else obj.Vision

    truncated_vision.short_description = 'Vision'

    def truncated_core_values(self , obj):
        return obj.Core_values[:50] + '...' if len(obj.Core_values) > 50 else obj.Core_values

    truncated_core_values.short_description = 'Core Values'