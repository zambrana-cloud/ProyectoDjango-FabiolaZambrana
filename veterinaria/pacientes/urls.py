from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet)
router.register(r'veterinarios', views.VeterinarioViewSet)
router.register(r'historia_clinica', views.HistoriaClinicaViewSet)
router.register(r'citas', views.CitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from .views import CitasPorPaciente

urlpatterns += [
    path('paciente/<int:paciente_id>/citas/', CitasPorPaciente.as_view(), name='citas_por_paciente'),
    path('api/', include('rest_framework.urls')),
]
