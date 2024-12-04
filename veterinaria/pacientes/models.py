from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Validaciones
def validate_nombre(value):
    if not value.strip():
        raise ValidationError("El nombre no puede estar vacío.")
    
def validate_edad(value):
    if value < 0:
        raise ValidationError("La edad no puede ser negativa.")

def validate_especie_otros(value, especie_otra):
    if value == 'otros' and not especie_otra.strip():
        raise ValidationError("Debe ingresar un nombre para la especie si selecciona 'Otros'.")

# Modelo Paciente
class Paciente(models.Model):
    ESPECIES_CHOICES = [
        ('canina', 'Canina'),
        ('felina', 'Felina'),
        ('ave', 'Ave'),
        ('otros', 'Otros'),
    ]
    UNIDAD_EDAD_CHOICES = [
        ('años', 'Años'),
        ('meses', 'Meses'),
    ]
    nombre = models.CharField(max_length=100, validators=[validate_nombre])
    especie = models.CharField(max_length=50, choices=ESPECIES_CHOICES)
    especie_otra = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(validators=[validate_edad])
    unidad_edad = models.CharField(max_length=5, choices=UNIDAD_EDAD_CHOICES, default='años')
    raza = models.CharField(max_length=100)
    nombre_dueño = models.CharField(max_length=100, blank=True, null=True, default='Desconocido')


    def clean(self):
        # Valida si se selecciona "otros" y no se llena el campo "especie_otra"
        validate_especie_otros(self.especie, self.especie_otra)
    
    def __str__(self):
        return self.nombre


class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class HistoriaClinica(models.Model):
    GRAVEDAD_CHOICES = [
        ('emergencia', 'Emergencia'),
        ('moderada', 'Moderada'),
        ('leve', 'Leve'),
    ]

    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    enfermedades = models.TextField()
    tratamientos = models.TextField()
    gravedad = models.CharField(max_length=10, choices=GRAVEDAD_CHOICES, default='leve')

    def __str__(self):
        return f"Historial de {self.paciente.nombre}"


class Cita(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Cita para {self.paciente.nombre} con {self.veterinario.nombre}"
