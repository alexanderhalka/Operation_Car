@echo off
echo void setup() {} void loop() {} > blank/blank.ino
arduino-cli compile --fqbn arduino:avr:uno blank
arduino-cli upload -p COM4 --fqbn arduino:avr:uno blank 