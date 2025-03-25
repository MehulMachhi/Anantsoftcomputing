from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Survey
from .serializers import SurveySerializer

class SurveyListCreateAPIView(ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


