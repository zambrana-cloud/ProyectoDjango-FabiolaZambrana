from rest_framework import serializers
from .models import Paciente, Veterinario, HistoriaClinica, Cita

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nombre', 'especie', 'especie_otra', 'edad', 'raza', 'nombre_dueño']

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono']

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'enfermedades', 'tratamientos', 'gravedad']  
class CitaSerializer(serializers.ModelSerializer):
    nombre_dueño = serializers.CharField(source='paciente.nombre_dueño', read_only=True)

    class Meta:
        model = Cita
        fields = ['paciente', 'veterinario', 'fecha', 'motivo', 'estado','nombre_dueño'] 

