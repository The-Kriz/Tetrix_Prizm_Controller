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
    prizm.setMotorPowers(50,50); 
  }
  else
  {
   prizm.setMotorPowers(125,125); 
  }   
}
