#define MQ2 A2 //define la entrada analogica para el sensor
#define RL_VALOR 5 //define el valor de la resistencia de carga en kilo ohms
#define RAL 9.83 // resistencia del sensor en el aire limpio / RO, que se deriva de la tabla de la hoja de datos
float Ro = 10;
void setup(){
Serial.begin(9600); //Inicializa Serial a 9600 baudios
 Serial.println("Iniciando ...");
   //configuracion del sensor
  Serial.print("Calibrando...\n");
  Ro = Calibracion(MQ2); //Calibrando el sensor. Por favor de asegurarse que el sensor se encuentre en una zona de aire limpio mientras se calibra
  Serial.print("Calibracion finalizada...\n");
  Serial.print("Ro=");
  Serial.print(Ro);
  Serial.print("kohm");
  Serial.print("\n");
}
 
void loop()
{
  
}
 
float calc_res(int lectura_actual_adc)
{
  return ( ((float)RL_VALOR*(1023-lectura_actual_adc)/lectura_actual_adc));
}
 
float Calibracion(float mq_pin){
  int i;
  float val=0;
    for (i=0;i<50;i++) { //tomar múltiples muestras
    val += calc_res(analogRead(mq_pin));
    delay(500);
  }
  val = val/50; //calcular el valor medio
  val = val/RAL;
  return val;
}

