from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PsychologistViewSet, ConsultationViewSet

router = DefaultRouter()
router.register(r'psychologists', PsychologistViewSet)
router.register(r'consultations', ConsultationViewSet)

# O URLconf do app
urlpatterns = [
    path('', include(router.urls)),
]
