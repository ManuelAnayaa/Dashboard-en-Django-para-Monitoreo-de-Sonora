import random
import paho.mqtt.client as mqtt_client


def connect_mqtt(broker, port, client_id, username=None, password=None):
    """
    Función reutilizable para conexión MQTT
    """

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("✅ Conectado al Broker MQTT!")
            print(f"📡 Broker: {broker}:{port}")
            print(f"🎯 Client ID: {client_id}")
        else:
            error_codes = {
                1: "Protocol version incorrecta",
                2: "Client identifier inválido",
                3: "Servidor no disponible",
                4: "Usuario o contraseña incorrectos",
                5: "No autorizado"
            }
            error_msg = error_codes.get(rc, f"Código de error desconocido: {rc}")
            print(f"❌ Error de conexión: {error_msg}")

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("⚠️  Desconexión inesperada del broker")
        else:
            print("🔌 Desconexión normal del broker")

    # Crear cliente MQTT
    client = mqtt_client.Client(client_id)

    # Configurar credenciales si se proporcionan
    if username and password:
        client.username_pw_set(username, password)

    # Configurar callbacks
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Conectar al broker
    try:
        client.connect(broker, port)
        return client
    except Exception as e:
        print(f"🚨 Error al conectar: {e}")
        return None