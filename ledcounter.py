import RPi.GPIO as GPIO
import time

LED_PIN = 17

#Set GPIO pins to Broadcom SOC channel naming convention
GPIO.setmode(GPIO.BCM) 
#Set GPIO pin to an output
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_pin, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
