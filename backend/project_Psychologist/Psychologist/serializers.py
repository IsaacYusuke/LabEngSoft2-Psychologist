from rest_framework import serializers
from .models import Psychologist, Consultation, Patient

class PsychologistSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField()
    scheduled_consultations = serializers.SerializerMethodField()
    profile_picture = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Psychologist
        fields = '__all__'  # Certifique-se de incluir os novos campos aqui, se estiver listando campos especificamente

    def get_available_slots(self, obj):
        # Aqui, assumimos que available_slots retorna uma estrutura de dados serializável, como lista ou dicionário
        return obj.available_slots

    def get_scheduled_consultations(self, obj):
        # Aqui, 'scheduled_consultations' é tratado como uma propriedade.
        # Supondo que você queira retornar uma lista de IDs de consulta ou algum outro dado simplificado
        consultations = obj.scheduled_consultations
        return ConsultationSerializer(consultations, many=True).data

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
