#include <PRIZM.h>   

PRIZM prizm;        

void setup() 
{
  prizm.PrizmBegin();
  prizm.setMotorInvert(1,1);    
}

void loop() 
{
  if(prizm.readSonicSensorCM(4) > 25) 
  {
    prizm.setMotorPowers(35,35);      
    prizm.setRedLED(LOW);   
    prizm.setGreenLED(HIGH); 
  }
  else
  {
   prizm.setGreenLED(LOW);
   prizm.setRedLED(HIGH); 
   prizm.setMotorPowers(125,125);
   delay(500);
   prizm.setMotorPowers(-35,-35);
   delay(1000);
   prizm.setMotorPowers(125,125);
   delay(500);
   prizm.setMotorPowers(35,-35);    
   delay(500);
  }   
}
