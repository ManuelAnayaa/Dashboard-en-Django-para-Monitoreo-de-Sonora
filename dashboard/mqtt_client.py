import paho.mqtt.client as mqtt_client
import random
import time

# --- Configuración ---
BROKER = 'broker.emqx.io'
PORT = 1883
TOPIC = "sonora/#"
CLIENT_ID = f'django-dashboard-{random.randint(0, 1000)}'

mqtt_data = {}


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("✅ Conectado al Broker MQTT!")
            client.subscribe(TOPIC)
        else:
            print(f"❌ Error de conexión: {rc}")

    client = mqtt_client.Client(CLIENT_ID)
    client.on_connect = on_connect

    try:
        client.connect(BROKER, PORT)
    except Exception as e:
        print(f"🚨 Error de conexión: {e}")

    return client


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"📥 Recibido: {topic} -> {payload}")

    # 1. Guardar en memoria para gráfica
    mqtt_data[topic] = payload

    # 2. GUARDAR EN BASE DE DATOS + ALERTA
    try:
        from monitoreo.models import DatoSensor
        partes = topic.split('/')

        if len(partes) == 3:
            municipio = partes[1]
            variable = partes[2]
            valor_float = float(payload)

            # --- NUEVO: SISTEMA DE ALERTAS ---
            # Si es temperatura y supera los 40 grados...
            if variable == 'temperatura' and valor_float > 40:
                print("\n" + "=" * 40)
                print(f"🔥 ¡ALERTA DE CALOR EN {municipio.upper()}! 🔥")
                print(f"   Temperatura crítica: {valor_float}°C")
                print("=" * 40 + "\n")
            # ---------------------------------

            # Crear registro en BD
            DatoSensor.objects.create(
                municipio=municipio,
                tipo_dato=variable,
                valor=valor_float
            )
            print("💾 Guardado en Base de Datos")

    except Exception as e:
        print(f"⚠️ Error: {e}")


def start_mqtt():
    client = connect_mqtt()
    client.on_message = on_message
    client.loop_start()