#include <Arduino.h>
const int LED_PIN = 9;  // Using pin 9 which is PWM capable

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);  // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    
    // Check if it's an LED command
    if (input.startsWith("LED ")) {
      // Extract the PWM value
      int pwm_value = input.substring(4).toInt();
      // Ensure value is in valid range
      pwm_value = constrain(pwm_value, 0, 255);
      // Set LED brightness
      analogWrite(LED_PIN, pwm_value);
    }
  }
}   