from django.db import models
from datetime import datetime, timedelta, time
#import requests

# Create your models here.

class Psychologist(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    document = models.CharField(max_length=15, unique=True, blank=False, null=True)
    start_time_morning = models.TimeField()
    end_time_morning = models.TimeField()
    start_time_afternoon = models.TimeField()
    end_time_afternoon = models.TimeField()
    consultation_price = models.DecimalField(max_digits=10, decimal_places=2)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    class Meta: 
        db_table = "psychologist"
    
    def __str__(self):
        return f"({self.pk}) {self.full_name}"

    def get_available_slots(self, days=30):
        """
        Retorna os horários disponíveis para o psicólogo nos próximos 'days' dias.
        """
        available_slots = []
        consultations = self.consultations.all()
        today = datetime.now().date()
        for day in range(days):
            date = today + timedelta(days=day)
            for slot in self._generate_daily_slots(date):
                if not consultations.filter(scheduled_time=slot).exists():
                    available_slots.append(slot)
        return available_slots

    def _generate_daily_slots(self, date):
        """
        Gera todos os slots de horário possíveis para um dia específico, baseado nos horários de atendimento.
        """
        slots = []
        morning_start = datetime.combine(date, self.start_time_morning)
        morning_end = datetime.combine(date, self.end_time_morning)
        afternoon_start = datetime.combine(date, self.start_time_afternoon)
        afternoon_end = datetime.combine(date, self.end_time_afternoon)

        while morning_start < morning_end:
            slots.append(morning_start)
            morning_start += timedelta(hours=1)
        
        while afternoon_start < afternoon_end:
            slots.append(afternoon_start)
            afternoon_start += timedelta(hours=1)

        return slots

    def get_scheduled_consultations(self, status=None):
        """
        Retorna as consultas agendadas para o psicólogo, opcionalmente filtradas por status.
        """
        if status:
            return self.consultations.filter(status=status)
        return self.consultations.all()
    
    @property
    def available_slots(self):
        # Implementação do método que retorna os slots disponíveis
        return self.get_available_slots()

    @property
    def scheduled_consultations(self):
        # Implementação do método que retorna as consultas agendadas
        # Aqui você poderia diretamente retornar as consultas sem precisar de um método separado
        return self.consultations.all()
    
    """
    def get_user_info(self):
    """
        #Retorna as informações do usuário associado a este psicólogo,
        #fazendo uma chamada à API externa onde os dados do usuário são gerenciados.
    """
        try:
            response = requests.get(f'http://outroprojeto.com/api/users/{self.id_user}/')
            if response.status_code == 200:
                # Assume-se que a API retorna um JSON com as informações do usuário
                return response.json()
            else:
                response.raise_for_status()
        except requests.RequestException as e:
            # Aqui você pode decidir como lidar com erros:
            # Você pode registrar o erro, lançar uma exceção customizada, etc.
            print(f'Erro ao buscar informações do usuário: {e}')

    """


class Consultation(models.Model):
    STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    psychologist = models.ForeignKey(Psychologist, related_name='consultations', on_delete=models.CASCADE)
    id_patient = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Requested')
    scheduled_time = models.DateTimeField()
    payment_proof = models.FileField(upload_to='payment_proofs/', null=True, blank=True)

    class Meta:
        # Isso garante que não haja sobreposição de horários para um psicólogo ou paciente
        constraints = [
            models.UniqueConstraint(fields=['psychologist', 'scheduled_time'], name='unique_scheduled_time_for_psychologist'),
            models.UniqueConstraint(fields=['id_patient', 'scheduled_time'], name='unique_scheduled_time_for_patient'),
        ]