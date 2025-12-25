void setup() {
  Serial.begin(9600);   // UART initialization
}

void loop() {
  Serial.println("Hello from ESP32");
  delay(1000);
}