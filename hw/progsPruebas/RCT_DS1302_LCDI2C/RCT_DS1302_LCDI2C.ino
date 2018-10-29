/*
////////////////////////////////////////////////////////////////////////////////////
//   AUTOR: Manuel Hidalgo - LeoBot                                     Octubre/2018
////////////////////////////////////////////////////////////////////////////////////
//   PROGRAMA: Comunicacion I2C con LCD y RTC (DS1302)          VERSIÓN:       1.0
//   DISPOSITIVO: ATMEL 328                                     COMPILADOR:    AVR
//   Entorno IDE:   1.8.5                                       SIMULADOR:     
//   TARJETA DE APLICACIÓN: ARDUINO                             DEBUGGER:     
////////////////////////////////////////////////////////////////////////////////////
MOSTRAR LCD_I2C Y MONITOR SERIE FECHA Y HORA DE UN RTC DS1302
////////////////////////////////////////////////////////////////////////////////////
*/

// Librerias
#include <Wire.h>
#include "DS1302RTC.h"
#include "LiquidCrystal_I2C.h"
#include "Time.h"

//Configuracion

// Inicializacion del modulo.
// El primer pin es para el RST, el segundo para DATA(I/O) y el tercero para CLK
DS1302RTC rtc(2, 3, 5);
time_t t;                          // variable t, desde la que le pediremos los datos
LiquidCrystal_I2C lcd(0x27,20,4);  // direccion LCD (16x2)

void setup() {
  
  lcd.init();                      //inicializacion LCD
  lcd.backlight();

  rtc.haltRCT(false);
  rtc.writeProtect(false); // comandos para poder escribir en el reloj, para setearle fecha y hora

  rtc.setDOW(SUNDAY);
  rtc.setTime(16, 34, 00);
  rtc.setDate(06, 11, 2016);

  Serial.begin(9600); // Inicializacion del puerto serie.
  Wire.begin(); // inicializacion de comunicaciones I2C
  
}

void loop() {
  // put your main code here, to run repeatedly:

}
