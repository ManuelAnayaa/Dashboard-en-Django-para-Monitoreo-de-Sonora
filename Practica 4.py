import random
import time
import paho.mqtt.client as mqtt_client

# Configuración MQTT
broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-sonora-{random.randint(1000, 9999)}'

# Wildcard a suscribir (MODIFICAR ESTA LÍNEA).
WILDCARD = "sonora/+"
#asadf

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Conectado. Suscrito a: {WILDCARD}")
        else:
            print(f"Error conexión: {rc}")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_message(client, userdata, message):
    # Solo mostrar el dato recibido
    print(f"{message.topic} -> {message.payload.decode()}")

def run():
    client = connect_mqtt()
    client.on_message = on_message
    client.subscribe(WILDCARD)
    client.loop_forever()

if __name__ == '__main__':
    run()