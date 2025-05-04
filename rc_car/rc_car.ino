#include <Arduino.h>

// Motor control pins
const int MOTOR_FORWARD_PIN = 9;   // PWM pin for forward speed
const int MOTOR_BACKWARD_PIN = 10; // PWM pin for backward speed
const int MOTOR_LEFT_PIN = 11;     // PWM pin for left turn
const int MOTOR_RIGHT_PIN = 12;    // PWM pin for right turn

void setup() {
  // Set all motor pins as outputs
  pinMode(MOTOR_FORWARD_PIN, OUTPUT);
  pinMode(MOTOR_BACKWARD_PIN, OUTPUT);
  pinMode(MOTOR_LEFT_PIN, OUTPUT);
  pinMode(MOTOR_RIGHT_PIN, OUTPUT);
  
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    
    // Parse the command
    if (input.startsWith("F ")) {  // Forward command
      int speed = input.substring(2).toInt();
      speed = constrain(speed, 0, 255);
      analogWrite(MOTOR_FORWARD_PIN, speed);
      analogWrite(MOTOR_BACKWARD_PIN, 0);
    }
    else if (input.startsWith("B ")) {  // Backward command
      int speed = input.substring(2).toInt();
      speed = constrain(speed, 0, 255);
      analogWrite(MOTOR_BACKWARD_PIN, speed);
      analogWrite(MOTOR_FORWARD_PIN, 0);
    }
    else if (input.startsWith("L ")) {  // Left command
      int speed = input.substring(2).toInt();
      speed = constrain(speed, 0, 255);
      analogWrite(MOTOR_LEFT_PIN, speed);
      analogWrite(MOTOR_RIGHT_PIN, 0);
    }
    else if (input.startsWith("R ")) {  // Right command
      int speed = input.substring(2).toInt();
      speed = constrain(speed, 0, 255);
      analogWrite(MOTOR_RIGHT_PIN, speed);
      analogWrite(MOTOR_LEFT_PIN, 0);
    }
    else if (input == "STOP") {  // Stop all motors
      analogWrite(MOTOR_FORWARD_PIN, 0);
      analogWrite(MOTOR_BACKWARD_PIN, 0);
      analogWrite(MOTOR_LEFT_PIN, 0);
      analogWrite(MOTOR_RIGHT_PIN, 0);
    }
  }
} 