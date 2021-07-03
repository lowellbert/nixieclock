#Get time and display time on nixie tube clock

from datetime import datetime
from time import sleep

import RPi.GPIO as GPIO

BINARY_OUTPUT_A = 17
BINARY_OUTPUT_B = 18
BINARY_OUTPUT_C = 22
BINARY_OUTPUT_D = 23

#Set GPIO pins to Broadcom SOC channel naming convention
GPIO.setmode(GPIO.BCM) 
#Set GPIO pin to an output
GPIO.setup(BINARY_OUTPUT_A, GPIO.OUT)
GPIO.setup(BINARY_OUTPUT_B, GPIO.OUT)
GPIO.setup(BINARY_OUTPUT_C, GPIO.OUT)
GPIO.setup(BINARY_OUTPUT_D, GPIO.OUT)

def main():
    while True:
        time = get_time()
        time_in_binary = convert_time_to_BCD(time)
        print(str(time_in_binary))
        send_BCD_to_pins(time_in_binary)


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    return current_time

def convert_time_to_BCD(time):
    print("Convert time to BCD")

    #split time into hours, minutes and seconds
    time_list = time.split(":")
    hour = time_list[0]
    minute = time_list[1]
    second = time_list[2]

    #split hours into two seperate digits
    hour_1st_digit = hour[0:1]
    hour_2nd_digit = hour[1:2]

    #split minutes into two seperate digits
    minute_1st_digit = minute[0:1]
    minute_2nd_digit = minute[1:2]

    #split seconds into two seperate digits
    second_1st_digit = second[0:1]
    second_2nd_digit = second[1:2]

    #convert into binary
    binary_of_hour_1st_digit = bin(int(hour_1st_digit))
    binary_of_hour_2nd_digit = bin(int(hour_2nd_digit))

    binary_of_minute_1st_digit = bin(int(minute_1st_digit))
    binary_of_minute_2nd_digit = bin(int(minute_2nd_digit))

    binary_of_second_1st_digit = bin(int(second_1st_digit))
    binary_of_second_2nd_digit = bin(int(second_2nd_digit))

    return binary_of_hour_1st_digit, binary_of_hour_2nd_digit, binary_of_minute_1st_digit, binary_of_minute_2nd_digit, binary_of_second_1st_digit, binary_of_second_2nd_digit

def send_BCD_to_pins(time_in_binary):
    #take first position of time_in_binary which is binary_of_hour_1st_digit
    nibble_of_hour_1st_digit = binary_to_nibble(time_in_binary[0])

    #Send 1st digit in hour to Raspberry Pi pins
    nibble_to_pins(nibble_of_hour_1st_digit)

    sleep(1)
    
    #take second position of time_in_binary which is binary_of_hour_2nd_digit
    nibble_of_hour_2nd_digit = binary_to_nibble(time_in_binary[1])

    #Send 1st digit in hour to Raspberry Pi pins
    nibble_to_pins(nibble_of_hour_2nd_digit)
    

def binary_to_nibble(time_in_binary):
    #remove 0b in binary number system
    time_in_binary = time_in_binary[2:]

    #Add "0" to make it a 4 character nibblle
    if len(time_in_binary) == 1:
        nibble = ("000"+time_in_binary)
    elif len(time_in_binary) == 2:
        nibble = ("00"+time_in_binary)
    elif len(time_in_binary) == 3:
        nibble = ("0"+time_in_binary)
    else:
        nibble = time_in_binary

    return nibble

def nibble_to_pins(nibble_of_hour_1st_digit):
     #Send 1st digit in hour to Raspberry Pi pins
    if nibble_of_hour_1st_digit[0] == str(1):
        #OUTPUT D
        print("send 1")
        GPIO.output(BINARY_OUTPUT_D, GPIO.HIGH)
    else:
        print("send 0")
        GPIO.output(BINARY_OUTPUT_D, GPIO.LOW)

    if nibble_of_hour_1st_digit[1] == str(1):
        #OUTPUT C
        print("send 1")
        GPIO.output(BINARY_OUTPUT_C, GPIO.HIGH)
    else:
        print("send 0")
        GPIO.output(BINARY_OUTPUT_C, GPIO.LOW)
    
    if nibble_of_hour_1st_digit[2] == str(1):
        #OUTPUT B
        print("send 1")
        GPIO.output(BINARY_OUTPUT_B, GPIO.HIGH)
    else:
        print("send 0")
        GPIO.output(BINARY_OUTPUT_B, GPIO.LOW)

    if nibble_of_hour_1st_digit[3] == str(1):
        #OUTPUT A
        print("send 1")
        GPIO.output(BINARY_OUTPUT_A, GPIO.HIGH)
    else:
        print("send 0")
        GPIO.output(BINARY_OUTPUT_A, GPIO.LOW)




main()
GPIO.cleanup()