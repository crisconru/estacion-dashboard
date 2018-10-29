/*Projecto EducaCont -- Estacion de Calidad del Aire
 * Noviembre 2018 -- Manuel Hidalgo -- LeoBot -- @leobotmanuel
 * 
 * Sensores conectados a Arduino UNO
 * DTH22 -- pin digital D6
 * 
 */

#include "DHT.h"

//Descomentar el tipo de sensor usado // Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

#define DHTPIN 6            // pin digital de DHT22
DHT dht(DHTPIN, DHTTYPE);   //declaracion del objeto dht

void setup() {
  Serial.begin(9600);
  Serial.println("Test de sensores Proyecto EducaCont:");

  dht.begin();
}

void loop() {
  //------------------------ sensor DHT22 --------------------------------------
  //---------------Lectura temperatura y humedad -------------------------------
  //Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  //-------------- Lectura de la sensasion termica -----------------------------
  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");



   // Wait a few seconds between measurements.
  delay(2000);
}
