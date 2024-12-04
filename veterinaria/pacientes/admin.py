from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Paciente, Veterinario, HistoriaClinica, Cita
from django.templatetags.static import static
from django.utils.html import format_html


class CustomAdminSite(AdminSite):
    site_title = "Mi Administrador Veterinaria"  
    site_header = "Panel de Control de Veterinaria"  
    index_title = "Bienvenido al Panel de Administración"

  
    def each_context(self, request):
        context = super().each_context(request) 
        context['extra_css'] = static('pacientes/css/admin.css')  
        return context

admin.site = CustomAdminSite()


def edad_con_unidad(paciente):
    return f"{paciente.edad} {paciente.unidad_edad}"

edad_con_unidad.short_description = 'Edad'
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'especie_otra', 'edad','unidad_edad','raza','nombre_dueño']
    list_filter = ['especie'] 
    search_fields = ['nombre', 'especie', 'especie_otra']
    fieldsets = (
        (None, {
            'fields': ('nombre', 'especie', 'especie_otra', 'edad', 'unidad_edad', 'raza', 'nombre_dueño')
        }),
    )
admin.site.register(Paciente, PacienteAdmin)


class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'telefono']
    list_filter = ['especialidad']  
    search_fields = ['nombre', 'especialidad']

admin.site.register(Veterinario, VeterinarioAdmin)

class CitaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'veterinario', 'fecha', 'motivo', 'estado']
    list_filter = ['estado']  
    search_fields = ['paciente__nombre','fecha', 'veterinario__nombre', 'motivo']

admin.site.register(Cita, CitaAdmin)

class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'enfermedades', 'gravedad']
    search_fields = ['paciente__nombre']
    list_filter = ['gravedad']

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)
  


