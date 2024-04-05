from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PsychologistViewSet, ConsultationViewSet, ConsultationsTodayView, PsychologistDataView

router = DefaultRouter()
router.register(r'psychologists', PsychologistViewSet)
router.register(r'consultations', ConsultationViewSet)

# O URLconf do app
urlpatterns = [
    path('consultations/today/', ConsultationsTodayView.as_view(), name='consultations-today'),
    path('psychologist_data/', PsychologistDataView.as_view(), name='psychologist-data'),
    path('', include(router.urls)),

]
