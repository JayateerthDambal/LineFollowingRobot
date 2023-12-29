import RPi.GPIO as GPIO

# GPIO setup for relay control
LEFT_MOTOR_RELAY_PIN = 17  # Replace with your GPIO pin
RIGHT_MOTOR_RELAY_PIN = 27  # Replace with your GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_MOTOR_RELAY_PIN, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_RELAY_PIN, GPIO.OUT)


def forward():
    GPIO.output(LEFT_MOTOR_RELAY_PIN, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_RELAY_PIN, GPIO.HIGH)


def backward():
    GPIO.output(LEFT_MOTOR_RELAY_PIN, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_RELAY_PIN, GPIO.LOW)


def turn_left():
    GPIO.output(LEFT_MOTOR_RELAY_PIN, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_RELAY_PIN, GPIO.HIGH)


def turn_right():
    GPIO.output(LEFT_MOTOR_RELAY_PIN, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_RELAY_PIN, GPIO.LOW)


def stop():
    GPIO.output(LEFT_MOTOR_RELAY_PIN, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_RELAY_PIN, GPIO.LOW)
