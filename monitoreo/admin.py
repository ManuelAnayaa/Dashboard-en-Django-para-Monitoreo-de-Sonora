from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import DatoSensor


# Función para exportar a CSV
def exportar_a_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos_iot.csv"'

    writer = csv.writer(response)
    # Escribir encabezados
    writer.writerow(['Fecha', 'Municipio', 'Variable', 'Valor'])

    # Escribir datos seleccionados
    for dato in queryset:
        writer.writerow([dato.fecha_registro, dato.municipio, dato.tipo_dato, dato.valor])

    return response


exportar_a_csv.short_description = "📄 Exportar seleccionados a CSV"


@admin.register(DatoSensor)
class DatoSensorAdmin(admin.ModelAdmin):
    list_display = ('fecha_registro', 'municipio', 'tipo_dato', 'valor')
    list_filter = ('municipio', 'tipo_dato')

    # Aquí agregamos la nueva acción al menú desplegable
    actions = [exportar_a_csv]