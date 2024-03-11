from django.shortcuts import render
from rest_framework import viewsets
from .models import Psychologist, Consultation
from .serializers import PsychologistSerializer, ConsultationSerializer

# Create your views here.

class PsychologistViewSet(viewsets.ModelViewSet):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
