#Get time and display time on nixie tube clock

from datetime import datetime

def main:
    get_time()
    convert_time_to_binary_coded_decimal()
    send_binary_coded_decimal_value_to_pins()

def get_time():
    now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)

def convert_time_to_binary_coded_decimal():
    #

def send_binary_coded_decimal_value_to_pins():
    #