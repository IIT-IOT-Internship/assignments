#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ---------- WiFi Credentials ----------
const char* ssid = "Reva";
const char* password = "Reva292005";

// ---------- MQTT Broker ----------
const char* mqtt_server = "test.mosquitto.org"; // public broker
const int mqtt_port = 1883;

// ---------- Topics ----------
const char* temp_topic = "sensor/temperature";
const char* hum_topic  = "sensor/humidity";

// ---------- DHT ----------
#define DHTPIN 4        // GPIO4
#define DHTTYPE DHT11   // DHT11 or DHT22

DHT dht(DHTPIN, DHTTYPE);

// ---------- Objects ----------
WiFiClient espClient;
PubSubClient client(espClient);

// ---------- WiFi Connect ----------
void setup_wifi() {
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

// ---------- MQTT Connect ----------
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  float temperature = dht.readTemperature(); // Celsius
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  char tempStr[10];
  char humStr[10];

  dtostrf(temperature, 4, 2, tempStr);
  dtostrf(humidity, 4, 2, humStr);

  client.publish(temp_topic, tempStr);
  client.publish(hum_topic, humStr);

  Serial.print("Temperature: ");
  Serial.print(tempStr);
  Serial.print(" °C | Humidity: ");
  Serial.print(humStr);
  Serial.println(" %");

  delay(5000); // publish every 5 seconds
}
