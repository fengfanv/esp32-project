import machine
import time

# 左电机
p32 = machine.Pin(13,machine.Pin.OUT)
p33 = machine.Pin(15,machine.Pin.OUT)

# # 左电机(前进)
# p32.value(0)
# p33.value(1)

# # 左电机(后退)
# p32.value(1)
# p33.value(0)

# 右电机
p12 = machine.Pin(14,machine.Pin.OUT)
p13 = machine.Pin(2,machine.Pin.OUT)

# # 右电机(前进)
# p12.value(1)
# p13.value(0)

# # 右电机(后退)
# p12.value(0)
# p13.value(1)


def car_up_open():
    # 左前进
    p32.value(0)
    p33.value(1)
    # 右前进
    p12.value(1)
    p13.value(0)

def car_up_close():
    p32.value(0)
    p33.value(0)
    p12.value(0)
    p13.value(0)

def car_down_open():
    # 左后退
    p32.value(1)
    p33.value(0)
    # 右后退
    p12.value(0)
    p13.value(1)

def car_down_close():
    p32.value(0)
    p33.value(0)
    p12.value(0)
    p13.value(0)

def car_left_open():
    # 左后退
    p32.value(1)
    p33.value(0)
    # 右前进
    p12.value(1)
    p13.value(0)

def car_left_close():
    p32.value(0)
    p33.value(0)
    p12.value(0)
    p13.value(0)

def car_right_open():
    # 左前进
    p32.value(0)
    p33.value(1)
    # 右后退
    p12.value(0)
    p13.value(1)

def car_right_close():
    p32.value(0)
    p33.value(0)
    p12.value(0)
    p13.value(0)
