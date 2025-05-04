@echo off
arduino-cli compile --fqbn arduino:avr:uno controller_interface
arduino-cli upload -p COM3 --fqbn arduino:avr:uno controller_interface