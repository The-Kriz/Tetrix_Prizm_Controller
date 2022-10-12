#include <PRIZM.h>
PRIZM prizm;

void setup()
{
  prizm.PrizmBegin();
}

void loop() 
{  
  if(prizm.readLineSensor(3) == HIGH) 
  {
    prizm.setRedLED(LOW);
  }
  if(prizm.readLineSensor(3) == LOW)
  {
    prizm.setRedLED(HIGH);
  }
  delay(50);
}
