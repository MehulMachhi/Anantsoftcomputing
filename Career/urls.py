from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet, JobLocationViewSet, SkillViewSet,
    JobPostingViewSet, EmployeeTestimonialViewSet, BenefitCategoryViewSet, JobApplicationView
)

router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
router.register('locations', JobLocationViewSet, basename='locations')
router.register('skills', SkillViewSet, basename='skills')
router.register('jobs', JobPostingViewSet, basename='jobs')
router.register('testimonials', EmployeeTestimonialViewSet, basename='testimonials')
router.register('benefits', BenefitCategoryViewSet, basename='benefits')

urlpatterns = [
    path('', include(router.urls)),
    path('jobapplication/', JobApplicationView.as_view()),
]