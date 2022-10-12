#include <PRIZM.h> 

PRIZM prizm;

void setup() 
{
  prizm.PrizmBegin();   // initialize the PRIZM controller
}

void loop() 
{
  prizm.setRedLED(HIGH);   
  delay(1000);         
  prizm.setRedLED(LOW);
  delay(1000);
}
