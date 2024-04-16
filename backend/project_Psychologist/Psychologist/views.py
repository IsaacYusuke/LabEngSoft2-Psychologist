from django.shortcuts import render
from rest_framework import viewsets
from .models import Psychologist, Consultation, Patient
from .serializers import PsychologistSerializer, ConsultationSerializer, PatientSerializer
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .models import Consultation #, Patient
from django.db.models import Count

# Create your views here.

    
class PsychologistView(ViewSet):
    def create(self, request):
        serializer = PsychologistSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Psychologist.objects.create(**serializer.validated_data)
        serializer = PsychologistSerializer(queryset)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    def list_all(self, request):
        queryset = Psychologist.objects.all()
        serializer = PsychologistSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Psychologist.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PsychologistSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)



class ConsultationView(ViewSet):
    def create(self, request):
        serializer = ConsultationSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Consultation.objects.create(**serializer.validated_data)
        serializer = ConsultationSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list_all(self, request):
        queryset = Consultation.objects.all()
        serializer = ConsultationSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_psychologist(self, request, prof):
        queryset = Consultation.objects.filter(psychologist=prof)
        serializer = ConsultationSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Consultation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ConsultationSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PatientView(ViewSet):
    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Patient.objects.create(**serializer.validated_data)
        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def list_all(self, request):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_psychologist(self, request, prof):
        queryset = Consultation.objects.filter(psychologist=prof)
        serializer = ConsultationSerializer(queryset, many=True)
        
        patient_list = [x['patient'] for x in serializer.data]
        queryset = Patient.objects.filter(pk__in=patient_list)
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        queryset = Patient.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
