#include <PRIZM.h>
PRIZM prizm;

int Break = 125;
int motorPower = 50;

void setup() 
{
  prizm.PrizmBegin();
  prizm.setMotorInvert(1,1);
}
void loop() {
  prizm.setMotorPowers(motorPower,motorPower);
  delay(3000);  
  prizm.setMotorPowers(Break,Break);
  delay(1000);                     
  prizm.setMotorPowers(motorPower,(motorPower*-1));    
  delay(600);
  prizm.setMotorPowers(Break,Break);
  delay(1000);    
  prizm.setMotorPowers(motorPower,motorPower);   
  delay(3000);                   
  prizm.setMotorPowers(Break,Break);   
  delay(1000);                    
  prizm.setMotorPowers(motorPower,(motorPower*-1));   
  delay(600);                     
  prizm.setMotorPowers(Break,Break);   
  delay(1000);                   
  prizm.setMotorPowers(motorPower,motorPower);      
  delay(3000);                     
  prizm.setMotorPowers(Break,Break);   
  delay(1000);                     
  prizm.setMotorPowers(motorPower,(motorPower*-1));    
  delay(600);                       
  prizm.setMotorPowers(Break,Break);  
  delay(1000);                      
  prizm.setMotorPowers(motorPower,motorPower);      
  delay(3000);                      
  prizm.setMotorPowers(Break,Break);   
  delay(1000);                     
  prizm.PrizmEnd();
}
