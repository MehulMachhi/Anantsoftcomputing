# contact/models.py
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

class ContactInformation(models.Model):
    """Model to store company contact information displayed on the website"""
    company_name = models.CharField(max_length=200 , default="Anant Soft Computing")
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20 , blank=True)
    email_primary = models.EmailField()
    email_secondary = models.EmailField(blank=True)

    # Working Hours
    working_hours_weekday = models.CharField(max_length=100 , default="Monday - Friday: 9:00 AM - 6:00 PM")
    working_hours_weekend = models.CharField(max_length=100 , default="Saturday: 9:00 AM - 2:00 PM")

    # Social Media Links
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    # Map Information
    map_embed_url = models.URLField(help_text="Google Maps Embed URL")
    latitude = models.DecimalField(max_digits=9 , decimal_places=6 , null=True , blank=True)
    longitude = models.DecimalField(max_digits=9 , decimal_places=6 , null=True , blank=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return self.company_name


class ServiceType(models.Model):
    """Model for services that can be selected in contact form"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ContactEnquiry(models.Model):
    """Model to store contact form submissions"""
    STATUS_CHOICES = [
        ('new' , 'New') ,
        ('in_progress' , 'In Progress') ,
        ('contacted' , 'Contacted') ,
        ('closed' , 'Closed') ,
    ]

    # Basic Information
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20 , blank=True)
    company = models.CharField(max_length=200 , blank=True)
    service = models.ForeignKey(ServiceType , on_delete=models.SET_NULL , null=True , blank=True)
    message = models.TextField()

    # Meta Information
    ip_address = models.GenericIPAddressField(null=True , blank=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(blank=True)

    # Status and Tracking
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Enquiry from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"

    # def send_notification_emails(self):
    #     """Send notification emails to admin and visitor"""
    #     # Admin notification
    #     admin_context = {
    #         'enquiry': self ,
    #         'admin_url': f"{settings.SITE_URL}/admin/contact/contactenquiry/{self.id}/change/"
    #     }
    #     admin_html = render_to_string('contact/email/admin_notification.html' , admin_context)
    #     admin_text = render_to_string('contact/email/admin_notification.txt' , admin_context)

    #     send_mail(
    #         subject=f"New Contact Enquiry from {self.name}" ,
    #         message=admin_text ,
    #         from_email=settings.DEFAULT_FROM_EMAIL ,
    #         recipient_list=[settings.ADMIN_EMAIL] ,
    #         html_message=admin_html
    #     )

    #     # Visitor notification
    #     visitor_context = {
    #         'enquiry': self ,
    #         'company_info': ContactInformation.objects.first()
    #     }
    #     visitor_html = render_to_string('contact/email/visitor_notification.html' , visitor_context)
    #     visitor_text = render_to_string('contact/email/visitor_notification.txt' , visitor_context)

    #     send_mail(
    #         subject="Thank you for contacting us" ,
    #         message=visitor_text ,
    #         from_email=settings.EMAIL_HOST_USER ,
    #         recipient_list=[self.email] ,
    #         html_message=visitor_html
    #     )
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None  
        super().save(*args, **kwargs)
        if is_new: 
            self.send_thank_you_email()

    def send_thank_you_email(self):
        service_template_map = {
            "Digital Strategy": "emails/consulting_email.html",
            "CRM Development": "emails/crm_email.html",
            "Custom Development": "emails/custom_development_email.html",
            "Mobile Apps": "emails/mobile_application_email.html",
            "SEO Optimization": "emails/seo_email.html",
            "ERP Systems": "emails/erp_systems_email.html"
        }
    
        if self.service:
            template_name = service_template_map.get(self.service.name)
        else:
            template_name = None
    
        if template_name:
            context = {
                "name": self.name,
                "email": self.email,
                "phone": self.phone,
                "company": self.company,
                "message": self.message,
                "service": self.service.name if self.service else "N/A",
            }
            html_content = render_to_string(template_name, context)
    
            email = EmailMessage(
                subject=f"Thank you for choosing {self.service.name}",
                body=html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[self.email],  
                cc=["anantsoftcomputing@gmail.com"],  
            )
            email.content_subtype = "html" 
            email.send()
        else:
            send_mail(
                subject="Thank you for contacting us",
                message="Thank you for contacting us. We will get back to you shortly.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.email],
                cc=["anantsoftcomputing@gmail.com"],  
            )