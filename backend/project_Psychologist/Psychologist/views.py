from django.shortcuts import render
from rest_framework import viewsets
from .models import Psychologist, Consultation
from .serializers import PsychologistSerializer, ConsultationSerializer
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Consultation #, Patient
from django.db.models import Count

# Create your views here.

class PsychologistViewSet(viewsets.ModelViewSet):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    
class PsychologistDataView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        psychologist_id = request.user.id  # Assumindo que você tem o ID do psicólogo associado ao usuário

        consultations_count = Consultation.objects.filter(psychologist_id=psychologist_id).count()
        # Supondo que cada consulta tenha um campo 'patient' que referencia um objeto Patient
        #patients_count = Patient.objects.annotate(num_consultations=Count('consultation')).filter(consultation__psychologist_id=psychologist_id).distinct().count()

        # Supondo que 'consultation_price' é um campo no modelo do psicólogo e cada consulta tem um 'scheduled_time'
        from django.db.models import Sum
        from django.utils import timezone
        month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        monthly_income = Consultation.objects.filter(psychologist_id=psychologist_id, scheduled_time__gte=month_start).aggregate(total=Sum('psychologist__consultation_price'))['total'] or 0

        return Response({
            'consultations_count': consultations_count,
            #'patients_count': patients_count,
            'monthly_income': monthly_income
        })


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationsTodayView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        psychologist_id = request.user.id
        today_start = now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = now().replace(hour=23, minute=59, second=59, microsecond=999999)

        consultations_today = Consultation.objects.filter(psychologist_id=psychologist_id, scheduled_time__range=(today_start, today_end))

        # Aqui você precisaria serializar suas consultas
        # Por simplicidade, vamos apenas retornar a contagem
        return Response({
            'consultations_today_count': consultations_today.count()
            # Para retornar objetos completos, você usaria um serializer para converter os objetos de consulta em JSON
        })
