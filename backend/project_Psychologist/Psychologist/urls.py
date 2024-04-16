from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PsychologistView, ConsultationView, PatientView

"""
router = DefaultRouter()
router.register(r'psychologists', PsychologistViewSet)
router.register(r'consultations', ConsultationViewSet)
"""

# O URLconf do app
urlpatterns = [
    path('psychologist/list/', PsychologistView.as_view({'get': 'list_all'})),
    path('psychologist/create/', PsychologistView.as_view({'post': 'create'})),
    path('psychologist/<int:pk>/', PsychologistView.as_view({'get': 'retrieve'})),
    path('consultation/list/', ConsultationView.as_view({'get': 'list_all'})),
    path('consultation/create/', ConsultationView.as_view({'post': 'create'})),
    path('consultation/<int:pk>/', ConsultationView.as_view({'get': 'retrieve'})),
    path('consultation/list/<int:prof>/', ConsultationView.as_view({'get': 'list_from_psychologist'})),
    path('patient/list/', PatientView.as_view({'get': 'list_all'})),
    path('patient/create/', PatientView.as_view({'post': 'create'})),
    path('patient/<int:pk>/', PatientView.as_view({'get': 'retrieve'})),
    path('patient/list/<int:prof>/', PatientView.as_view({'get': 'list_from_psychologist'})),
]
