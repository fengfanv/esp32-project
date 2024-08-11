class Daikuan:
    datetimeModule = None  # datetime模块
    osModule = None  # os模块
    printCount = 0  # 打印次数（测试次数）

    lastTime = 0
    now = 0
    sizeCount = 0

    def __init__(self):
        # self.datetimeModule = __import__("datetime")
        # self.osModule = __import__("os")
        self.datetimeModule = __import__("time")

    def get_timestamp(self):
        # return self.datetimeModule.datetime.now().timestamp() * 1000  # 将秒转成毫秒
        return self.datetimeModule.ticks_ms()

    def clear_print(self):
        # if self.osModule.name == 'nt':
        #     self.osModule.system("cls")  # 以下适用于Windows系统
        # else:
        #     self.osModule.system("clear")  # 以下适用于Linux/Mac系统
        return None
    
    def update(self, size):
        self.now = self.get_timestamp()

        self.sizeCount += size  # //记录1秒钟内，累计接收到的数据包大小

        if self.now - self.lastTime >= 1000:
            # 如果已经过去1秒，则计算每秒能传输多少字节数据
            speed = (self.sizeCount / (self.now - self.lastTime)) * 1000

            # self.clear_print()

            print("网速1："+str(round(speed, 2))+" Byte/s | "+str(round(speed / 1024, 2))+" KByte/s | "+str(round(speed / 1024 / 1024, 2))+" MByte/s")
            print("网速2："+str(round(speed * 8, 2))+" bit/s | "+str(round(speed * 8 / 1024, 2))+" Kbit/s | "+str(round(speed * 8 / 1024 / 1024, 2))+" Mbit/s")

            self.sizeCount = 0
            self.lastTime = self.now

            self.printCount += 1  # 记录打印次数

'''
daikuan = Daikuan()
isLoop = True
chunk = 'a'.encode()
while isLoop:
    daikuan.update(len(chunk))
    if daikuan.printCount >= 10:
        isLoop = False
'''