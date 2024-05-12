# 舵机控制（MG90S）
from machine import Pin,PWM
import time

can_run = True
def toDeg(deg):
    global can_run
    if can_run == True:
        can_run = False
        
        p4 = PWM(Pin(12))
        p4.freq(50) # 为啥这里设置频率值(50Hz)? 厂商规定舵机的一个pwm周期时长20ms(毫秒)。20ms转Hz是 { 1/(20/1000)=50 } 1是1秒，20/1000是将毫秒转成秒
    
        if deg == 0:
            # int((0.5/20)*65535)=>1638 在一个时长为20ms的pwm周期内，高电平持续时长为0.5ms时，舵机转动到0度。将高电平的持续时长(ms,毫秒)转成这里的占空比(比例值)
            p4.duty_u16(1638)
        elif deg == 45:
            # int((1/20)*65535)=>3276 在一个时长为20ms的pwm周期内，高电平持续时长为1ms时，舵机转动到45度。将高电平的持续时长(ms,毫秒)转成这里的占空比(比例值)
            p4.duty_u16(3276)
        elif deg == 90:
            # int((1.5/20)*65535)=>4915 在一个时长为20ms的pwm周期内，高电平持续时长为1.5ms时，舵机转动到90度。将高电平的持续时长(ms,毫秒)转成这里的占空比(比例值)
            p4.duty_u16(4915)
        elif deg == 135:
            # int((2/20)*65535)=>6553 在一个时长为20ms的pwm周期内，高电平持续时长为2ms时，舵机转动到135度。将高电平的持续时长(ms,毫秒)转成这里的占空比(比例值)
            p4.duty_u16(6553)
        elif deg == 180:
            # int((2.5/20)*65535)=>8191 在一个时长为20ms的pwm周期内，高电平持续时长为2.5ms时，舵机转动到180度。将高电平的持续时长(ms,毫秒)转成这里的占空比(比例值)
            p4.duty_u16(8191)
    
        time.sleep(0.2)
        p4.deinit() # 停止PWM并释放引脚。解决舵机转动到某个角度时，舵机会呲呲响的问题
        
        can_run = True

'''
toDeg(180)
print('当前是180deg')
time.sleep(3)

toDeg(135)
print('当前是135deg')
time.sleep(3)

toDeg(90)
print('当前是90deg')
time.sleep(3)

toDeg(45)
print('当前是45deg')
time.sleep(3)

toDeg(0)
print('当前是0deg')
time.sleep(3)

toDeg(90) # 恢复成90deg
print('当前是90deg')
'''
