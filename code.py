#Created by: Osamah
#Created on: APR 2025
#Servo Control with Ultrasonic Sensor

import board
import pwmio
import time
import adafruit_hcsr04
from adafruit_motor import servo

# Define pins
trigPin = board.GP3
echoPin = board.GP2
servoPin = board.GP4

# Setup Ultrasonic Sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=trigPin, echo_pin=echoPin)

# Setup PWM for servo
pwm = pwmio.PWMOut(servoPin, duty_cycle=0, frequency=50)
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

# Servo angles
angleone = 0
angletwo = 90
anglethree = 180
servostop = 1  # In seconds

while True:
    try:
        distance = sonar.distance
        print(f"Distance: {distance} cm")
        
        # Check if distance is less than 5 cm before each movement
        if distance < 5:
            my_servo.angle = angletwo  # Move to 90 degrees
            time.sleep(servostop)

        distance = sonar.distance
        if distance < 5:
            my_servo.angle = angleone  # Move to 0 degrees
            time.sleep(servostop)

        distance = sonar.distance
        if distance < 5:
            my_servo.angle = anglethree  # Move to 180 degrees
            time.sleep(servostop)

        distance = sonar.distance
        if distance < 5:
            my_servo.angle = angleone  # Move to 0 degrees
            time.sleep(servostop)

        time.sleep(0.1)  # Small delay to avoid excessive readings

    except RuntimeError:
        print("Retrying...")
        time.sleep(0.1)
