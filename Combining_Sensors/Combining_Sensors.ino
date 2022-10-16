#include <PRIZM.h>    
 
 PRIZM prizm;           

void setup() 
{
  prizm.PrizmBegin();        
  prizm.setMotorInvert(1,1);                     
  prizm.setServoSpeed(1,50);                     
}

void loop() 
{
  if(prizm.readLineSensor(3) == 1)
  {
    prizm.setMotorPowers(30,125);  
    prizm.setRedLED(HIGH);
  }
  else
  {
    prizm.setMotorPowers(125,30);
    prizm.setRedLED(LOW);
  }  
  while(prizm.readSonicSensorCM(4) < 25)
  {  
    prizm.setGreenLED(HIGH);        
    prizm.setMotorPowers(125,125);    
    prizm.setServoPosition(1,0); 
  }
  prizm.setGreenLED(LOW);            
  prizm.setServoPosition(1,90);
}
