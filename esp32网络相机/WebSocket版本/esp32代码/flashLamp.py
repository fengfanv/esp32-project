def open():
    from machine import Pin
    try:
        Pin(4, Pin.OUT).value(1)
        return True
    except:
        return False

def close():
    from machine import Pin
    try:
        Pin(4, Pin.OUT).value(0)
        return True
    except:
        return False

