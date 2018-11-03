/*Projecto EducaCont -- Estacion de Calidad del Aire
 * Noviembre 2018 -- Manuel Hidalgo -- LeoBot -- @leobotmanuel
 * 
 * 
 * DS1302, modulo reloj:
 *          CE pin    -> Arduino pin Digital 2
 *          I/O pin   -> Arduino pin Digital 3
 *          SCLK pin  -> Arduino pin Digital 4
 *
 * Sensores conectados a Arduino UNO
 * DTH22 -- pin digital D6
 * 
 * MICS-4514 (NO2 y CO)
 *           PRE pin    -> Arduino pin Digital 7    //precalentamiento
 *           NOX        -> Arduino pin Analogico A0   //pin dato de NO2
 *           RED        -> Arduino pin Analogico A1   //pin dato de CO
 * 
 *  MQ-St
 *           AO         -> Arduino pin Analogico A2   //pin dato de MQ-St
 *           
 * Memoria microSD conectada al bus SPI bus:
 *           MOSI - pin 11
 *           MISO - pin 12
 *           CLK - pin 13
 *           CS - pin 9       
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

// ----------------- sensor MICS-4514 NO2 y CO  --------------------------
#define PRE_PIN          7    //precalentamiento
#define VNOX_PIN         A0   //pin dato de NO2
#define VRED_PIN         A1   //pin dato de CO

#define PRE_HEAT_SECONDS 10   //tiempo de precalentamiento

int vnox_value = 0;     //lectura dato de NO2
int vred_value = 0;     //lectura dato de CO

// ----------------- sensor MQ-St  --------------------------
#define MQ_St_PIN          A2    //pin dato de MQ-St

int vmq_st_value = 0;     //lectura dato de MQ-St

// ----------------- microSD  --------------------------
#include <SPI.h>
#include <SD.h>

const int chipSelect = 9;   //pin de seleccion microSD
String datos;               // vaiable datos
//===========================================================================
void setup() {
  Serial.begin(9600);   // inicializacion monitor serie
  Serial.println("Test de sensores Proyecto EducaCont:");
  Serial.println("  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -");

  rtc.halt(false);           //poner el reloj modo run           
  rtc.writeProtect(true);   //activado la protección write 

  dht.begin();    //inicializar el sensor DHT

  //----- Inicializacion sensor MICS-4514 ----------------
  // Setup preheater pin
  pinMode(PRE_PIN, OUTPUT);
  
  // Mensaje monitor serie
  Serial.println("MiCS-4514 Test Read");
  Serial.print("Precalentando...");

  // Wait for preheating
  digitalWrite(PRE_PIN, 1);
  delay(PRE_HEAT_SECONDS * 1000);
  digitalWrite(PRE_PIN, 0);
  Serial.println("Terminado");

  //----- Inicializacion sensor MQ-St ----------------
  // necesita entre 12 o 48 de calentamiento ¿? PENDIENTE

  //----- Inicializacion Memoria micoSD ----------------
  Serial.println("Inicializacion de la Tarjeta microSD...");
  // Comprueba que la tarjeta esta conectada
  if (!SD.begin(chipSelect)) {
    Serial.println("Tarjeta microSD no conectada");
    return;
  }
  Serial.println("MicroSD inicializada.");
  
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
  Serial.print("Sensacion termica: ");
  Serial.print(hic);
  Serial.print(" *C -- ");
  Serial.print(hif);
  Serial.println(" *F");
  Serial.println();

  //------------------------ sensor MICS-4514 ---------------------------
  //------------------------ Lectura NO2 y CO ---------------------------
  // Read analog values, print them out, and wait
  vnox_value = analogRead(VNOX_PIN);
  vred_value = analogRead(VRED_PIN);
  Serial.print("Nivel de NO2, (cod_A/D_Vnox): ");
  Serial.print(vnox_value, DEC);
  Serial.print(" -- Nivel de CO, (cod_A/D_Vred): ");
  Serial.println(vred_value, DEC);
  Serial.println();

  //------------------------ sensor MQ-St ---------------------------
  //------------------------ Lectura MQ-St ---------------------------
  // Read analog values, print them out, and wait
  vmq_st_value = analogRead(MQ_St_PIN);
  Serial.print("Nivel de MQ-St, (cod_A/D_vmq_st_value): ");
  Serial.println(vmq_st_value, DEC);
  Serial.println();

  datos = String (rtc.getDateStr()) + "," + String(rtc.getTimeStr()) + "," + String(h) + "," + String(tc) + "," + String(hic) + "," + String(vnox_value) + "," + String(vred_value) + "," + String(vmq_st_value);
  //------------------------ Memoria microSD -------------------------
  // Abrimos el fichero, si no existe lo crea
  File ficheroDatos = SD.open("datos.txt", FILE_WRITE);

   //Si el fichero esta habilitado, escribe // if the file is available, write to it:
  if (ficheroDatos) {
    ficheroDatos.println(datos);
    ficheroDatos.close();
    // Escribe en el monitor el valor de datos  // print to the serial port too:
    Serial.println(datos);
  }
  // Si no esta abierto, mensaje de error// if the file isn't open, pop up an error:
  else {
    Serial.println("error abriendo datos.txt");
  }
  
   //Espera 5 segundos ente medidas // Wait a few seconds between measurements.
  delay(5000);
}
