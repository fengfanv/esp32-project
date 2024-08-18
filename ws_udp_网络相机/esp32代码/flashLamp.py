from machine import Pin

def open():
    try:
        Pin(4, Pin.OUT).value(1)
        return True
    except:
        return False

def close():
    try:
        Pin(4, Pin.OUT).value(0)
        return True
    except:
        return False

