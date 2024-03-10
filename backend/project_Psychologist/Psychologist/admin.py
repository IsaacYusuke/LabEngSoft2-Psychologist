from django.contrib import admin
from .models import Psychologist, Consultation

# Register your models here.

class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email')

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'id_patient', 'status', 'scheduled_time')
    list_filter = ('status', 'scheduled_time')
    search_fields = ('psychologist__full_name', 'id_patient')

admin.site.register(Psychologist, PsychologistAdmin)
admin.site.register(Consultation, ConsultationAdmin)
