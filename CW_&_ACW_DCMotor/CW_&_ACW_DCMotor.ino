#include <PRIZM.h>

PRIZM prizm;
int motorPower = 25;

void setup() 
{        
  prizm.PrizmBegin();
}

void loop()
{
  prizm.setMotorPower(1,motorPower);
  delay(5000);                 
  prizm.setMotorPower(1,0);
  delay(2000);                 
  prizm.setMotorPower(1,(motorPower*-1));
  delay(5000);                
  prizm.setMotorPower(1,0);
  delay(2000);                 
}
