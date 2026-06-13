from machine import Pin
from utime import sleep
import time

from machine import Pin
import time

carGreen = Pin(8, Pin.OUT)
carYellow = Pin(9, Pin.OUT)
carRed = Pin(10, Pin.OUT)

pedGreen = Pin(16, Pin.OUT)
pedYellow = Pin(17, Pin.OUT)
pedRed = Pin(18, Pin.OUT)


def set_car(red, yellow, green):
    carRed.value(red)
    carYellow.value(yellow)
    carGreen.value(green)


def set_ped(red, yellow, green):
    pedRed.value(red)
    pedYellow.value(yellow)
    pedGreen.value(green)
    
def cars_green():
    set_car(0, 0, 1)
    set_ped(1, 0, 0)

def switch_to_pedestrians():

    # Grün, Orange
    set_car(0,1,0)
    time.sleep(2)

    # Rot
    set_car(1,0,0)
    time.sleep(1)

    # Grün
    set_ped(0,0,1)

    time.sleep(5)
    
    set_ped(0,1,0)
    time.sleep(1)

    # Rot
    set_ped(1,0,0)

    # Rot + Orange
    set_car(1,1,0)
    time.sleep(2)

    # Grün
    set_car(0,0,1)
    
waiting_cars = False
waiting_pedestrians = True

if waiting_pedestrians:
    switch_to_pedestrians()

carRed.off()
pedRed.off()
print("Finished.")