#include <PRIZM.h>
PRIZM prizm;

int motorPower = 50;

void setup() 
{
  prizm.PrizmBegin();    
  prizm.setMotorInvert(1,1);
}

void loop() 
{
  prizm.setMotorPowers(motorPower,motorPower);
  delay(3000);
  prizm.PrizmEnd();
}
