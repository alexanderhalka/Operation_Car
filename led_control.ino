const int ledPin = 9;  // LED connected to pin 9

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  pinMode(ledPin, OUTPUT);  // Set LED pin as output
}

void loop() {
  if (Serial.available() > 0) {  // Check if data is available to read
    char command = Serial.read();  // Read the incoming byte
    
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn LED on
    }
    else if (command == '0') {
      digitalWrite(ledPin, LOW);   // Turn LED off
    }
  }
} 