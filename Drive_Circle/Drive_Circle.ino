#include <PRIZM.h>
PRIZM prizm;

int motor1Power = 50;
int motor2Power = 25;

void setup() 
{
  prizm.PrizmBegin();    
  prizm.setMotorInvert(1,1);
}

void loop() 
{
  prizm.setMotorPowers(motor1Power,motor2Power);                          
}
