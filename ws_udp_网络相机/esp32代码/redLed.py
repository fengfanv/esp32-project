# GPIO 33 – 内置红色指示灯
from machine import Pin

def open():
    try:
        Pin(33, Pin.OUT).value(0)
        return True
    except:
        return False

def close():
    try:
        Pin(33, Pin.OUT).value(1)
        return True
    except:
        return False