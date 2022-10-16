#include <PRIZM.h>    

PRIZM prizm;         

void setup() 
{
  prizm.PrizmBegin();
  prizm.setMotorInvert(1,1);                           
}

void loop() 
{
  if(prizm.readLineSensor(3) == 0) 
  {
    prizm.setMotorPowers(35,35);     
  }                                                                    

  if(prizm.readLineSensor(3) == 1) 
  {
    prizm.setMotorPowers(125,125); 
    while(1)
    {             
      prizm.setRedLED(HIGH);
      delay(500);
      prizm.setRedLED(LOW);
      delay(500);
    }
  }
}
