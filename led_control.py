import serial
import keyboard
import time

# Connect to Arduino
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

print("LED Control Ready!")
print("Press 'w' or UP ARROW to turn LED on full")
print("Press 's' or DOWN ARROW to turn LED off")
print("Press 'a' or LEFT ARROW for half brightness")
print("Press 'd' or RIGHT ARROW for half brightness")
print("Press 'q' to quit")

try:
    while True:
        if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
            arduino.write(b'UP\n')
            time.sleep(0.1)  # Debounce
        elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):
            arduino.write(b'DOWN\n')
            time.sleep(0.1)  # Debounce
        elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
            arduino.write(b'LEFT\n')
            time.sleep(0.1)  # Debounce
        elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
            arduino.write(b'RIGHT\n')
            time.sleep(0.1)  # Debounce
        elif keyboard.is_pressed('q'):
            break
        
finally:
    arduino.close()
    print("\nProgram ended")
