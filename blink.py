from machine import Pin
from utime import sleep_ms, ticks_ms, ticks_diff

car_green_pin = Pin(8, Pin.OUT)
car_yellow_pin = Pin(9, Pin.OUT)
car_red_pin = Pin(10, Pin.OUT)

ped_green_pin = Pin(16, Pin.OUT)
ped_yellow_pin = Pin(17, Pin.OUT)
ped_red_pin = Pin(18, Pin.OUT)

def set_car(red, yellow, green):
    car_red.value(red)
    car_yellow.value(yellow)
    car_green.value(green)

def set_ped(red, yellow, green):
    ped_red.value(red)
    ped_yellow.value(yellow)
    ped_green.value(green)

def car_green():
    set_car(0, 0, 1)
    set_ped(1, 0, 0)
    
def car_to_red():
    set_car(0, 1, 0)
    sleep_ms(2000)
    set_car(1, 0, 0)
    
def car_to_red_yellow():
    set_car(1, 1, 0)
    sleep_ms(2000)
    set_car(0, 0, 1)

def pedestrian_green():
    set_ped(0, 0, 1)
    set_car(1, 0, 0)

def pedestrian_to_red():
    set_ped(0, 1, 0)
    sleep_ms(1000)
    set_ped(1, 0, 0)

def request_pedestrian():
    global pedestrian_request
    pedestrian_request = True

def update_traffic_light():
    global pedestrian_request, current, start_time

    now = ticks_ms()

    if current == "car_green":
        car_green()
        if pedestrian_request:
            car_to_red()
            pedestrian_green()
            current = "pedestrian_green"
            start_time = now
            pedestrian_request = False

    elif current == "pedestrian_green":
        pedestrian_green()
        if ticks_diff(now, start_time) >= 5000:
            pedestrian_to_red()
            car_to_red_yellow()
            current = "car_green"
            start_time = now

