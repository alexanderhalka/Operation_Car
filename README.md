# RC Car Control System

This project modifies a standard RC car so it can be controlled programmatically from a computer.

Instead of using only the physical remote buttons, I wired the remote to an Arduino and built a Python application that sends control commands over USB. The Arduino then simulates button presses electronically.

---

## Overview

The system has three main parts:

1. A modified RC remote connected to an Arduino  
2. A Python program that captures keyboard input  
3. Arduino firmware that converts commands into steering and throttle signals  

This allows real-time control of the RC car using a keyboard.

---

## Hardware Setup

- Opened the RC remote and identified the metal pads used by the steering and throttle buttons.
- Soldered wires to those button pads so they could be triggered externally.
- Used a transistor as an electronic switch so the Arduino could simulate pressing the buttons safely.
- Connected the Arduino output pins to the transistor, which triggers the remote circuit when activated.

---

## Software Architecture

### Python Controller
- Captures keyboard input
- Sends serial commands to the Arduino over USB
- Allows real-time control

### Arduino Firmware (C++)
- Listens for serial input
- Parses incoming commands
- Converts commands into output signals for steering and throttle

---

## Features

- Real-time keyboard-based control
- Separation between hardware control (Arduino) and user input logic (Python)
- Version controlled using Git
- Dependency management handled with Poetry
