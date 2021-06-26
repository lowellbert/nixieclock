import RPi.GPIO as GPIO
import time

BINARY_INPUT_A = 17
BINARY_INPUT_B = 18
BINARY_INPUT_C = 22
BINARY_INPUT_D = 23

#Set GPIO pins to Broadcom SOC channel naming convention
GPIO.setmode(GPIO.BCM) 
#Set GPIO pin to an output
GPIO.setup(BINARY_INPUT_A, GPIO.OUT)
GPIO.setup(BINARY_INPUT_B, GPIO.OUT)
GPIO.setup(BINARY_INPUT_C, GPIO.OUT)
GPIO.setup(BINARY_INPUT_D, GPIO.OUT)

#Set all outputs to low
def set_outputs_low():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)
    time.sleep(1)

def set_output_to_0():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_1():
    GPIO.output(BINARY_INPUT_A, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_2():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_3():
    GPIO.output(BINARY_INPUT_A, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_B, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_4():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_5():
    GPIO.output(BINARY_INPUT_A, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_6():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_C, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_7():
    GPIO.output(BINARY_INPUT_A, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_B, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_C, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_D, GPIO.LOW)

def set_output_to_8():
    GPIO.output(BINARY_INPUT_A, GPIO.LOW)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.HIGH)

def set_output_to_9():
    GPIO.output(BINARY_INPUT_A, GPIO.HIGH)
    GPIO.output(BINARY_INPUT_B, GPIO.LOW)
    GPIO.output(BINARY_INPUT_C, GPIO.LOW)
    GPIO.output(BINARY_INPUT_D, GPIO.HIGH)

def main():
    set_outputs_low()
    while True:
        set_output_to_0()
        time.sleep(1)
        set_output_to_1()
        time.sleep(1)
        set_output_to_2()
        time.sleep(1)
        set_output_to_3()
        time.sleep(1)
        set_output_to_4()
        time.sleep(1)
        set_output_to_5()
        time.sleep(1)
        set_output_to_6()
        time.sleep(1)
        set_output_to_7()
        time.sleep(1)
        set_output_to_8()
        time.sleep(1)
        set_output_to_9()
        time.sleep(1)

main()
GPIO.cleanup()
