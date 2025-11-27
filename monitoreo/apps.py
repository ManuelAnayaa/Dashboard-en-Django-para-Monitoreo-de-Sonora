from django.apps import AppConfig
import os

class MonitoreoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoreo'

    def ready(self):
        # Esta función se ejecuta cuando Django termina de cargar
        # El 'if' evita que se ejecute dos veces (una por el servidor y otra por el reloader)
        if os.environ.get('RUN_MAIN'):
            try:
                # CAMBIO AQUÍ: Importamos el módulo completo explícitamente
                import dashboard.mqtt_client as mqtt
                mqtt.start_mqtt()
                print("✅ Cliente MQTT iniciado correctamente")
            except Exception as e:
                print(f"⚠️ Error al iniciar MQTT: {e}")