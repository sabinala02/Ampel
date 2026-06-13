from machine import Pin
from utime import sleep_ms, ticks_ms, ticks_diff

car_green = Pin(8, Pin.OUT)
car_yellow = Pin(9, Pin.OUT)
car_red = Pin(10, Pin.OUT)

ped_green = Pin(16, Pin.OUT)
ped_yellow = Pin(17, Pin.OUT)
ped_red = Pin(18, Pin.OUT)

def set_car(red, yellow, green):
    car_red.value(red)
    car_yellow.value(yellow)
    car_green.value(green)

def set_ped(red, yellow, green):
    ped_red.value(red)
    ped_yellow.value(yellow)
    ped_green.value(green)

def cars_green():
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

def switch_to_pedestrians():
    set_car(0, 1, 0)
    sleep(2)
    set_car(1, 0, 0)
    sleep(1)

    set_car(1, 1, 0)
    sleep(2)
    set_car(0, 0, 1)

    set_ped(0, 0, 1)
    sleep(5)

    set_ped(0, 1, 0)
    sleep(1)
    set_ped(1, 0, 0)

    set_car(1, 1, 0)
    sleep(2)
    set_car(0, 0, 1)
    set_ped(1, 0, 0)