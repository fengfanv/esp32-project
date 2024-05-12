from machine import Pin

pin_4 = Pin(4, Pin.OUT)

def turnOn():
    pin_4.value(1)

def turnOff():
    pin_4.value(0)
    


