# Gesture-Control-Robotic-Hand
A real-time gesture-controlled robotic hand using OpenCV, MediaPipe, Arduino UNO, PCA9685, and servo motors. The system tracks finger movements through a webcam and mimics them on a robotic hand using five servo motors, enabling intuitive human-hand gesture replication.


# Gesture Control Robotic Hand

A real-time computer vision based robotic hand that mimics human finger movements using OpenCV, MediaPipe, Arduino UNO, PCA9685 Servo Driver, and 5 Servo Motors.

The system uses a webcam to detect hand landmarks and finger positions. Each finger of the human hand controls a dedicated servo motor, allowing the robotic hand to replicate finger movements in real time.

---

## Project Overview

Gesture Control Robotic Hand is a Human-Machine Interface (HMI) project that combines Computer Vision, Embedded Systems, Robotics, and Automation.

Using a laptop webcam, the system detects hand gestures and finger positions through MediaPipe Hand Tracking. The detected finger states are sent to an Arduino via serial communication. The Arduino then controls servo motors through a PCA9685 servo driver to mimic the user's hand movements.

This project demonstrates the integration of Artificial Intelligence, Computer Vision, and Robotics for real-time motion replication.

---

## Features

* Real-time hand tracking using webcam
* Finger detection using MediaPipe
* Individual control of five servo motors
* Real-time gesture replication
* Arduino and PCA9685 based servo control
* Low-cost robotic hand implementation
* Expandable for prosthetic and industrial applications
* Easy to build and customize

---

## Hardware Requirements

| Component                 | Quantity    |
| ------------------------- | ----------- |
| Arduino UNO               | 1           |
| PCA9685 Servo Driver      | 1           |
| Servo Motors (SG90/MG90S) | 5           |
| Robotic Hand Structure    | 1           |
| Jumper Wires              | As Required |
| USB Cable                 | 1           |
| External 5V Power Supply  | 1           |
| Laptop/PC with Webcam     | 1           |

---

## Software Requirements

* Python 3.11
* Arduino IDE
* OpenCV
* MediaPipe
* PySerial
* Adafruit PWM Servo Driver Library

---

## Working Principle

1. The webcam captures the user's hand.
2. OpenCV processes the video frames.
3. MediaPipe detects hand landmarks.
4. Finger positions are analyzed.
5. The Python program determines whether each finger is open or closed.
6. Finger data is sent to Arduino through serial communication.
7. Arduino receives the finger data.
8. PCA9685 generates PWM signals.
9. Servo motors move according to finger positions.
10. The robotic hand mimics the user's hand gesture.

---

## System Architecture

Human Hand

    ↓

Laptop Webcam

    ↓

OpenCV + MediaPipe

    ↓

Python Processing

    ↓

Serial Communication (USB)

    ↓

Arduino UNO

    ↓

PCA9685 Servo Driver

    ↓

5 Servo Motors

    ↓

Robotic Hand Movement

---

## Circuit Connections

### PCA9685 to Arduino UNO

| PCA9685 | Arduino UNO |
| ------- | ----------- |
| VCC     | 5V          |
| GND     | GND         |
| SDA     | A4          |
| SCL     | A5          |

---

### Servo Connections

| Finger | PCA9685 Channel |
| ------ | --------------- |
| Thumb  | Channel 0       |
| Index  | Channel 1       |
| Middle | Channel 2       |
| Ring   | Channel 3       |
| Pinky  | Channel 4       |

---

### External Power Supply

| Power Supply | PCA9685 |
| ------------ | ------- |
| +5V          | V+      |
| GND          | GND     |

Important: Connect Arduino GND and PCA9685 GND together.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Gesture-Control-Robotic-Hand.git
cd Gesture-Control-Robotic-Hand
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install opencv-python mediapipe pyserial
```

---

## Upload Arduino Code

1. Open Arduino IDE.
2. Install Adafruit PWM Servo Driver Library.
3. Connect Arduino UNO.
4. Select correct COM Port.
5. Upload the Arduino sketch.

---

## Run the Project

```bash
python hand_servo_control.py
```

Make sure the correct COM port is selected in the Python code.

Example:

```python
arduino = serial.Serial('COM3', 115200)
```

---

## Applications

* Prosthetic Hand Research
* Human Machine Interface Systems
* Gesture Controlled Robots
* Industrial Automation
* Teleoperation Systems
* Educational Robotics
* Computer Vision Learning
* Robotics Research Projects

---

## Future Improvements

* Smooth proportional finger tracking
* Wireless communication using ESP32
* Machine Learning based gesture recognition
* Full arm motion tracking
* VR and AR integration
* Haptic feedback system
* AI-powered gesture classification
* 3D printed robotic hand design

---

## Learning Outcomes

* Computer Vision
* OpenCV Programming
* MediaPipe Hand Tracking
* Arduino Programming
* Serial Communication
* Servo Motor Control
* Embedded Systems
* Robotics Integration
* Human Machine Interface Design

---

## Project Images

Add project images in the images folder and display them here.

```markdown
![Robotic Hand](images/robotic_hand.jpg)
```

---

## Author

Deepak Kumar Anand

B.Voc Robotics and Automation

Central University of Rajasthan

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgements

* OpenCV
* MediaPipe
* Arduino Community
* Adafruit
* Robotics and Automation Community

⭐ If you found this project useful, please consider giving it a star.
