from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PsychologistViewSet, ConsultationViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'psychologists', PsychologistViewSet)
router.register(r'consultations', ConsultationViewSet)

# O URLconf do app
urlpatterns = [
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
