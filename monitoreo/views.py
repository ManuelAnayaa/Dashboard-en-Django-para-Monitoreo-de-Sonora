from django.shortcuts import render
from django.http import JsonResponse
from dashboard.mqtt_client import mqtt_data  # Importamos los datos del MQTT
from .models import DatoSensor

# --- ESTA ES LA FUNCIÓN QUE TE FALTABA ---
def dashboard_view(request):
    return render(request, 'monitoreo/dashboard.html')

def get_data_api(request):
    """API para enviar los datos al JavaScript"""
    return JsonResponse(mqtt_data)