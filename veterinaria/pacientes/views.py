from django.shortcuts import render

from rest_framework import viewsets
from .models import Paciente, Veterinario, HistoriaClinica, Cita
from .serializers import PacienteSerializer, VeterinarioSerializer, HistoriaClinicaSerializer, CitaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cita
from .serializers import CitaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitasPorPaciente(APIView):
    def get(self, request, paciente_id, format=None):
        citas = Cita.objects.filter(paciente_id=paciente_id)
        serializer = CitaSerializer(citas, many=True)
        return Response




