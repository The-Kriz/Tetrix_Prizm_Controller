/*
  |X|X|X|X|
  |X|X|X|X|
  |X|X|X|X|
  |X|X|X|X|

  0 = move Forward
  1 = move Left
  2 = move Right
  3 = move Backward

*/

#include <PRIZM.h>
#include <SoftwareSerial.h>
#define rxPin 9
#define txPin 2
int motorPower = 50;

PRIZM prizm;
SoftwareSerial Btmodule (rxPin, txPin);
void setup() {
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  Btmodule.begin(9600);
  prizm.PrizmBegin();
  prizm.setMotorInvert(1, 1);
}


void moveFront() {
  prizm.setMotorTargets(360, 1440, 360, 1440);
}

void moveBack() {
  prizm.setMotorTargets(-360, -1440, -360, -1440);
}

void rotateLeft() {
  prizm.setMotorDegrees(180, 360, 180, 360);

}

void rotateRight() {
  prizm.setMotorDegrees(-180, -360, -180, -360);
}

void loop() {
  if (Btmodule.available() > 0) {
    int path = Btmodule.parseInt();
    Serial.print("I received: ");
    Serial.print(path);
    Serial.println();

    while (path > 0) {

      int x = path % 10;
      if ( x == 1) {
        moveFront();
      }
      else if ( x == 2) {
        rotateLeft();
      }
      else if ( x == 3) {
        rotateRight();
      }
      else if ( x == 4) {
        moveBack();
      }

      if (x == 9) {
        prizm.PrizmEnd();
      }
    }
  }
}
