/*Projecto EducaCont -- Estacion de Calidad del Aire
 * Noviembre 2018 -- Manuel Hidalgo -- LeoBot -- @leobotmanuel
 * 
 * 
 * DS1302, modulo reloj:
 *          CE pin    -> Arduino Digital 2
 *          I/O pin   -> Arduino Digital 3
 *          SCLK pin  -> Arduino Digital 4
 *
 * Sensores conectados a Arduino UNO
 * DTH22 -- pin digital D6
 * 
 */

// ------------------modulo reloj-----------------------
#include <DS1302.h>
// inicializacion del DS1302  // Init the DS1302
DS1302 rtc(2, 3, 5);
// declaracion objeto Time  // Init a Time-data structure
Time t;

// ----------------- sensor DHT --------------------------
#include <DHT.h>
//Descomentar el tipo de sensor usado // Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

#define DHTPIN 6            // pin digital de DHT22
DHT dht(DHTPIN, DHTTYPE);   //declaracion del objeto dht

//Variables sensor DHT
float h;    //humedad
float tc;    //Temperatura Celsius
float tf;    //Temperatura Fahrenheit
float hif;  //Sensacion termica Fahrenheit
float hic;  //Sensacion termica Celsius


void setup() {
  Serial.begin(9600);   // inicializacion monitor serie

  rtc.halt(false);           //poner el reloj modo run           
  rtc.writeProtect(true);   //activado la protección write 

  dht.begin();    //inicializar el sensor DHT
}

void loop() {
  Serial.println("Test de sensores Proyecto EducaCont:");
  Serial.println("  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -");

  // tomar datos del reloj  // Get data from the DS1302
  t = rtc.getTime();
  
  Serial.print(t.dow, DEC);
  Serial.print(" - ");
  Serial.print(rtc.getDateStr());
  Serial.print(" - ");
  Serial.println(rtc.getTimeStr());
  Serial.println();
  
  //------------------------ sensor DHT22 --------------------------------------
  //---------------Lectura temperatura y humedad -------------------------------
  //Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  tc = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  tf = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(tc) || isnan(tf)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  //-------------- Lectura de la sensasion termica -----------------------------
  // Compute heat index in Fahrenheit (the default)
  hif = dht.computeHeatIndex(tf, h);
  // Compute heat index in Celsius (isFahreheit = false)
  hic = dht.computeHeatIndex(tc, h, false);

  // Escribir datos del DHT22 en el monitor serie
  Serial.print("Humedad: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(tc);
  Serial.print(" *C -- ");
  Serial.print(tf);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C -- ");
  Serial.print(hif);
  Serial.println(" *F");
  Serial.println();



   // Wait a few seconds between measurements.
  delay(5000);
}
