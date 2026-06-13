from machine import Pin
from utime import sleep_ms, ticks_ms, ticks_diff

car_green_pin = Pin(8, Pin.OUT)
car_yellow_pin = Pin(9, Pin.OUT)
car_red_pin = Pin(10, Pin.OUT)

ped_green_pin = Pin(16, Pin.OUT)
ped_yellow_pin = Pin(17, Pin.OUT)
ped_red_pin = Pin(18, Pin.OUT)

pedestrian_request = False
current = "car_green"
start_time = ticks_ms()

def set_car(red, yellow, green):
    car_red_pin.value(red)
    car_yellow_pin.value(yellow)
    car_green_pin.value(green)

def set_ped(red, yellow, green):
    ped_red_pin.value(red)
    ped_yellow_pin.value(yellow)
    ped_green_pin.value(green)

def car_green():
    set_car(0, 0, 1)
    set_ped(1, 0, 0)
    
def car_yellow():
    set_car(0, 1, 0)
    set_ped(1, 0, 0)
    
def car_red():
    set_car(0, 1, 0)
    set_car(1, 0, 0)
    
def car_red_yellow():
    set_car(1, 1, 0)
    set_ped(1, 0, 0)

def pedestrian_green():
    set_ped(0, 0, 1)
    set_car(1, 0, 0)

def pedestrian_yellow():
    set_car(1, 0, 0)
    set_ped(0, 1, 0)

def request_pedestrian():
    global pedestrian_request
    pedestrian_request = True
    
def request_car():
    global car_request
    car_request = True

def update_traffic_light():
    global pedestrian_request, car_request, current, start_time

    now = ticks_ms()

    if current == "car_green":
        car_green()
        if pedestrian_request:
            car_yellow()
            sleep_ms(2000)
            car_red()
            sleep_ms(1000)
            pedestrian_green()
            current = "pedestrian_green"
            start_time = ticks_ms()
            pedestrian_request = False

    elif current == "pedestrian_green":
        pedestrian_green()
        if ticks_diff(now, start_time) >= 5000 or car_request:
            pedestrian_yellow()
            sleep_ms(1000)
            car_red_yellow()
            sleep_ms(2000)
            car_green()
            current = "car_green"
            start_time = ticks_ms()
            car_request = False