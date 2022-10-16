#include <PRIZM.h>  

PRIZM prizm;   
void setup() 
{
  prizm.PrizmBegin(); 
  prizm.setMotorInvert(1,1); 
}
void loop() 
{
  if(prizm.readLineSensor(3) == 0){prizm.setMotorPowers(125,30); prizm.setRedLED(LOW);}  
  if(prizm.readLineSensor(3) == 1){prizm.setMotorPowers(30,125); prizm.setRedLED(HIGH);} 
   
}
