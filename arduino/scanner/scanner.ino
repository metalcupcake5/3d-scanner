#include <Servo.h>

Servo servoX;
Servo servoY;

int sensorPin = A0;
int sensorValue = 0;
int servoXPos = 90;
int servoYPos = 90;
int rotateDelay = 50;

int posX = 0;
int posY = 0;
int forward = 0;
int step = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
  servoX.write(50);
  servoY.write(50);
}

void loop() {
  delay(10000);
  Serial.println("starting");
  // put your main code here, to run repeatedly:
  for (posX = 60; posX <= 125; posX += 1) {
    servoX.write(posX);
    if (forward == 0) {
      for(posY = 125; posY >= 60; posY -= 1) {
        servoY.write(posY);
        delay(rotateDelay);
        sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
      }
    } else {
      for (posY = 60; posY <= 125; posY += 1) {
        servoY.write(posY);
        delay(rotateDelay);
        sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
      }
    } 
    forward = forward == 1 ? 0 : 1;
    delay(rotateDelay);
  }
  Serial.println("DONE");
  delay(100000);
  /*
  for (posX = 130; posX >= 50; posX -= 1) {
    servoX.write(posX);
    Serial.println("aaa");
    for (posY = 130; posY >= 50; posY -= 1) {
      servoY.write(posY);
      sensorValue = analogRead(sensorPin);
      Serial.println(sensorValue);
      delay(rotateDelay);
    }
    delay(rotateDelay);
  }
  */
}

