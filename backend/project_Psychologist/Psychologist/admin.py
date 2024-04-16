from django.contrib import admin
from .models import Psychologist, Consultation, Patient

# Register your models here.

admin.site.register(Psychologist)
admin.site.register(Consultation)
admin.site.register(Patient)