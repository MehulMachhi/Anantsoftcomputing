from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectTechstackViewSet,
    ProjectKeyFeatureViewSet,
    PortfolioCategoryViewSet,
    ProjectImpactViewSet
)

router = DefaultRouter()
router.register('techstack', ProjectTechstackViewSet, basename='techstack')
router.register('keyfeatures', ProjectKeyFeatureViewSet, basename='keyfeatures')
router.register('categories', PortfolioCategoryViewSet, basename='categories')
router.register('impacts', ProjectImpactViewSet, basename='impacts')

urlpatterns = [
    path('', include(router.urls)),
]