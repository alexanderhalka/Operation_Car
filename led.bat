@echo off
arduino-cli compile --fqbn arduino:avr:uno led_pwm
arduino-cli upload -p COM4 --fqbn arduino:avr:uno led_pwm 