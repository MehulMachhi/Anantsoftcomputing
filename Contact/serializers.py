from rest_framework import serializers
from .models import ContactInformation , ServiceType , ContactEnquiry


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = [
            'id' , 'company_name' , 'address_line1' , 'address_line2' ,
            'city' , 'state' , 'postal_code' , 'phone_primary' ,
            'phone_secondary' , 'email_primary' , 'email_secondary' ,
            'working_hours_weekday' , 'working_hours_weekend' ,
            'linkedin_url' , 'twitter_url' , 'github_url' , 'instagram_url' ,
            'map_embed_url' , 'latitude' , 'longitude'
        ]


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id' , 'name' , 'slug' , 'is_active']


class ContactEnquirySerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name' , read_only=True)

    class Meta:
        model = ContactEnquiry
        fields = [
            'id' , 'name' , 'email' , 'phone' , 'company' ,
            'service' , 'service_name' , 'message' , 'status' ,
            'created_at' , 'updated_at'
        ]
        read_only_fields = ['status' , 'created_at' , 'updated_at']

    def create(self , validated_data):
        # Get client IP and user agent from request
        request = self.context.get('request')
        if request:
            validated_data['ip_address'] = request.META.get('REMOTE_ADDR')
            validated_data['user_agent'] = request.META.get('HTTP_USER_AGENT')
            validated_data['referrer'] = request.META.get('HTTP_REFERER' , '')

        # Create the enquiry
        enquiry = ContactEnquiry.objects.create(**validated_data)

        # Send notification emails
        try:
            enquiry.send_notification_emails()
        except Exception as e:
            print(f"Failed to send notification emails: {e}")

        return enquiry