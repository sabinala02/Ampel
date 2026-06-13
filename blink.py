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


def set_ped(red, green):
    pedRed.value(red)
    pedGreen.value(green)

while True:
    try:
        carGreen.value(1)
        carYellow.value(0)
        carRed.value(0)
        
        pedGreen.value(0)
        pedYellow.value(0)
        pedRed.value(1)
        
        time.sleep(3)
        
        carGreen.value(0)
        carYellow.value(0)
        carRed.value(1)
        
        pedGreen.value(1)
        pedYellow.value(0)
        pedRed.value(0)
        
        
    except KeyboardInterrupt:
        break
    sleep(1) # sleep 1sec

onBoard.off()
carRed.off()
pedRed.off()
print("Finished.")

