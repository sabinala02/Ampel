from machine import Pin
from utime import sleep
import time

onBoard = Pin("LED", Pin.OUT)
carGreen = Pin(8, Pin.OUT)
carRed = Pin(10, Pin.OUT)
carYellow = Pin(9, Pin.OUT)

pedestrianRed = Pin(18, Pin.OUT)
pedestrianYellow = Pin(17, Pin.OUT)
pedestrianGreen = Pin(16, Pin.OUT)

while True:
    try:
        carGreen.value(1)
        carYellow.value(0)
        carRed.value(0)
        
        pedestrianGreen.value(0)
        pedestrianYellow.value(0)
        pedestrianRed.value(1)
        
        time.sleep(3)
        
        carGreen.value(0)
        carYellow.value(0)
        carRed.value(1)
        
        pedestrianGreen.value(1)
        pedestrianYellow.value(0)
        pedestrianRed.value(0)
        
        
    except KeyboardInterrupt:
        break
    sleep(1) # sleep 1sec

onBoard.off()
carRed.off()
pedestrianRed.off()
print("Finished.")
