import sys
import queue
from enum import Enum
import pygame
from pygame.locals import *
try:
    import serial.serialutil
    from serial import Serial, SerialException
    SERIAL_AVAILABLE = True
except ImportError:
    print("Warning: pyserial not installed. Running in debug mode.")
    SERIAL_AVAILABLE = False

class Direction(Enum):
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"

class KeyboardInputHandler:
    def __init__(self, input_queue):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Keyboard Control")
        pygame.key.set_repeat(100, 50)  # Enable key repeat (delay, interval)
        self.running = True
        self.input_queue = input_queue
        self.speed = 50  # Initial PWM duty cycle (0-100%)
        self.key_map = {
            K_w: Direction.FORWARD,
            K_UP: Direction.FORWARD,
            K_a: Direction.LEFT,
            K_LEFT: Direction.LEFT,
            K_s: Direction.BACKWARD,
            K_DOWN: Direction.BACKWARD,
            K_d: Direction.RIGHT,
            K_RIGHT: Direction.RIGHT
        }
        # Try to connect to serial port with error handling
        self.ser = None
        if SERIAL_AVAILABLE:
            try:
                self.ser = Serial('COM3', 9600, timeout=1)
            except (SerialException, OSError) as e:
                print(f"Warning: Could not open serial port: {e}")
                print("Running in debug mode without serial communication")
        else:
            print('Serial port not available')

    def send_command(self, direction, speed):
        # First send the original command for printing

        # Then send LED control command
        # Convert speed (0-100) to PWM value (0-255)
        pwm_value = 255 - int((speed / 100.0) * 255)
        command_str = f"{direction.value[0].upper()} {pwm_value}\n"
        print(f"Sending command: {command_str}")
        
        
        if self.ser is None:
            print(f"Debug mode - would send LED command: {command_str}")
            return
            
        self.ser.write(command_str.encode())

    def get_next_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key in self.key_map:
                    direction = self.key_map[event.key]
                    self.input_queue.put((direction, self.speed))
                    print(f"Direction: {direction.value}, Speed: {self.speed}%")
                    self.send_command(direction, self.speed)
                    # Send a stop command immediately for single press
                    if not pygame.key.get_pressed()[event.key]:
                        self.send_command(Direction.FORWARD, 0)  # Send 0 speed to stop
                elif event.key == K_LSHIFT or event.key == K_RSHIFT:
                    self.speed = min(self.speed + 10, 100)
                    print(f"Speed/Brightness increased: {self.speed}%")
                elif event.key == K_LCTRL or event.key == K_RCTRL:
                    self.speed = max(self.speed - 10, 0)
                    print(f"Speed/Brightness decreased: {self.speed}%")
            elif event.type == KEYUP:
                # When key is released, send stop command
                if event.key in self.key_map:
                    self.send_command(Direction.FORWARD, 0)  # Send 0 speed to stop
        
        # Check for held keys
        keys = pygame.key.get_pressed()
        for key_code, direction in self.key_map.items():
            if keys[key_code]:
                self.input_queue.put((direction, self.speed))
                self.send_command(direction, self.speed)
        
        return None

    def run(self):
        print("Press WASD or arrow keys to move. Press ESC to exit.")
        print("Hold SHIFT to increase speed/brightness, CTRL to decrease speed/brightness.")
        while self.running:
            self.screen.fill((0, 0, 0))  # Clear screen
            pygame.display.flip()  # Update display
            self.get_next_input()
        pygame.quit()
        if self.ser:
            self.ser.close()
        print("Game loop exited successfully.")

if __name__ == "__main__":
    input_queue = queue.Queue()
    handler = KeyboardInputHandler(input_queue)
    handler.run()

    while not input_queue.empty():
        direction, speed = input_queue.get()
        print(f"Received input: {direction.value}, Speed: {speed}%")
