from datetime import datetime

now = datetime.now()

def get_time():
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

get_time()