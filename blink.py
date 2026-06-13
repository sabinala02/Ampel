from machine import Pin
from utime import sleep_ms, ticks_ms, ticks_diff

car_green_pin = Pin(8, Pin.OUT)
car_yellow_pin = Pin(9, Pin.OUT)
car_red_pin = Pin(10, Pin.OUT)

ped_green_pin = Pin(16, Pin.OUT)
ped_yellow_pin = Pin(17, Pin.OUT)
ped_red_pin = Pin(18, Pin.OUT)

pedestrian_request = False
car_request = False
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

def show_car_green():
    set_car(0, 0, 1)
    set_ped(1, 0, 0)

def show_car_yellow():
    set_car(0, 1, 0)
    set_ped(1, 0, 0)

def show_car_red():
    set_car(1, 0, 0)
    set_ped(1, 0, 0)

def show_car_red_yellow():
    set_car(1, 1, 0)
    set_ped(1, 0, 0)

def show_ped_green():
    set_car(1, 0, 0)
    set_ped(0, 0, 1)

def show_ped_yellow():
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
        show_car_green()
        if pedestrian_request:
            show_car_yellow()
            sleep_ms(2000)
            show_car_red()
            sleep_ms(1000)
            show_ped_green()
            current = "pedestrian_green"
            start_time = ticks_ms()
            pedestrian_request = False

    elif current == "pedestrian_green":
        show_ped_green()
        if ticks_diff(now, start_time) >= 5000 or car_request:
            show_ped_yellow()
            sleep_ms(1000)
            show_car_red_yellow()
            sleep_ms(2000)
            show_car_green()
            current = "car_green"
            start_time = ticks_ms()
            car_request = False

    elif current == "car_yellow":
        show_car_yellow()
        sleep_ms(2000)
        show_car_red()
        current = "car_red"
        start_time = ticks_ms()
    
    elif current == "car_red":
        show_car_red()
    
    elif current == "car_red_yellow":
        show_car_red_yellow()
        sleep_ms(2000)
        show_car_green()
        current = "car_green"
        start_time = ticks_ms()
    
    elif current == "pedestrian_yellow":
        show_ped_yellow()
        sleep_ms(1000)
        show_car_red_yellow()
        current = "car_red_yellow"
        start_time = ticks_ms()
