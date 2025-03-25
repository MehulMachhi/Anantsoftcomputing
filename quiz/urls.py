from django.urls import path
from .views import SurveyListCreateAPIView

urlpatterns = [
    path('surveys/', SurveyListCreateAPIView.as_view(), name='survey-list-create'),
]
