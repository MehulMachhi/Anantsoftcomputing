# contact/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import ContactInformation , ServiceType , ContactEnquiry


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Information' , {
            'fields': ('company_name' , 'address_line1' , 'address_line2' ,
                       'city' , 'state' , 'postal_code')
        }) ,
        ('Contact Details' , {
            'fields': ('phone_primary' , 'phone_secondary' ,
                       'email_primary' , 'email_secondary')
        }) ,
        ('Working Hours' , {
            'fields': ('working_hours_weekday' , 'working_hours_weekend')
        }) ,
        ('Social Media' , {
            'fields': ('linkedin_url' , 'twitter_url' , 'github_url' , 'instagram_url')
        }) ,
        ('Map Information' , {
            'fields': ('map_embed_url' , 'latitude' , 'longitude')
        }) ,
    )

    def has_add_permission(self , request):
        # Only allow one instance of ContactInformation
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' , 'is_active')
    prepopulated_fields = {'slug': ('name' ,)}
    list_filter = ('is_active' ,)
    search_fields = ('name' ,)


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'company' , 'service' , 'status' ,
                    'created_at' , 'action_buttons')
    list_filter = ('status' , 'service' , 'created_at')
    search_fields = ('name' , 'email' , 'company' , 'message')
    readonly_fields = ('created_at' , 'updated_at' , 'ip_address' ,
                       'user_agent' , 'referrer')

    fieldsets = (
        ('Contact Information' , {
            'fields': ('name' , 'email' , 'phone' , 'company')
        }) ,
        ('Enquiry Details' , {
            'fields': ('service' , 'message')
        }) ,
        ('Status & Notes' , {
            'fields': ('status' , 'admin_notes')
        }) ,
        ('Meta Information' , {
            'classes': ('collapse' ,) ,
            'fields': ('created_at' , 'updated_at' , 'ip_address' ,
                       'user_agent' , 'referrer')
        }) ,
    )

    def action_buttons(self , obj):
        return format_html(
            '<a class="button" href="mailto:{}">Email</a> &nbsp;'
            '<a class="button" href="tel:{}">Call</a>' ,
            obj.email ,
            obj.phone
        )

    action_buttons.short_description = 'Actions'