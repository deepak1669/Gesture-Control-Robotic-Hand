#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN 102
#define SERVOMAX 512

void setup() {
  Serial.begin(115200);

  pwm.begin();
  pwm.setPWMFreq(50);
}

int angleToPulse(int ang) {
  return map(ang, 0, 180, SERVOMIN, SERVOMAX);
}

void loop() {

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');

    int t, i, m, r, p;

    sscanf(data.c_str(), "%d,%d,%d,%d,%d",
           &t, &i, &m, &r, &p);

    pwm.setPWM(0, 0, angleToPulse(t));
    pwm.setPWM(1, 0, angleToPulse(i));
    pwm.setPWM(2, 0, angleToPulse(m));
    pwm.setPWM(3, 0, angleToPulse(r));
    pwm.setPWM(4, 0, angleToPulse(p));
  }
}