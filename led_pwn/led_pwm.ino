#include <Arduino.h>
const int LED_PIN = 9;  // Using pin 9 which is PWM capable on Arduino Mega

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Fade in
  for (int brightness = 0; brightness <= 255; brightness += 13) {
    analogWrite(LED_PIN, brightness);
    delay(100);
  }
  
  // Fade out
  for (int brightness = 255; brightness >= 0; brightness -= 13) {
    analogWrite(LED_PIN, brightness);
    delay(100);
  }
}   