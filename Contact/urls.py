from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactInformationViewSet,
    ServiceTypeViewSet,
    ContactEnquiryViewSet
)

router = DefaultRouter()
router.register('info', ContactInformationViewSet, basename='contact-info')
router.register('services', ServiceTypeViewSet, basename='contact-services')
router.register('enquiries', ContactEnquiryViewSet, basename='contact-enquiries')

urlpatterns = [
    path('', include(router.urls)),
]