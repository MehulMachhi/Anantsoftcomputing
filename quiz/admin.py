from django.contrib import admin
from .models import Survey
# Register your models here.

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('age_group', 'location', 'gender_identity', 'state_union_territory', 'education_level')
    list_filter = ('age_group', 'location', 'gender_identity', 'education_level', 'witnessed_violence')
    search_fields = ('state_union_territory', 'forms_of_violence', 'most_underreported_form')
