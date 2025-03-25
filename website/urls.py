from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestimonialsViewSet, PortfolioViewSet, AboutusViewSet

router = DefaultRouter()
router.register('testimonials', TestimonialsViewSet, basename='testimonials')
router.register('portfolio', PortfolioViewSet, basename='portfolio')
router.register('about', AboutusViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
]