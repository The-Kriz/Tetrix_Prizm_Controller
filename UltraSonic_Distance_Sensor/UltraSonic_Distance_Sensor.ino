#include <PRIZM.h> 

#define SonicSensorPin 3

PRIZM prizm;

void setup() 
{
  prizm.PrizmBegin();
  Serial.begin(9600);
}

void loop() 
{
  Serial.print(prizm.readSonicSensorCM(SonicSensorPin));
  Serial.println(" Centimeters");  
  delay(200);      
}
