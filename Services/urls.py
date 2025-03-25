from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceCategoryViewSet,
    ServiceViewSet,
    ServiceFeatureViewSet,
    ServiceImageViewSet
)

router = DefaultRouter()
router.register('categories', ServiceCategoryViewSet, basename='service-categories')
router.register('services', ServiceViewSet, basename='services')
router.register('features', ServiceFeatureViewSet, basename='service-features')
router.register('images', ServiceImageViewSet, basename='service-images')

urlpatterns = [
    path('', include(router.urls)),
]