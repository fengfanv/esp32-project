class Zhenshu:
    datetimeModule = None  # datetime模块
    printCount = 0  # 打印次数（测试次数）

    lastTime = 0
    now = 0
    frameCount = 0

    def __init__(self):
        # self.datetimeModule = __import__("datetime")
        self.datetimeModule = __import__("time")

    def get_timestamp(self):
        # return self.datetimeModule.datetime.now().timestamp() * 1000  # 将秒转成毫秒
        return self.datetimeModule.ticks_ms()

    def update(self):
        self.now = self.get_timestamp()

        self.frameCount += 1  # 记录1秒钟内被执行多次

        if self.now - self.lastTime >= 1000:
            # 如果已经过去1秒，则计算每秒的帧数
            fps = (self.frameCount / (self.now - self.lastTime)) * 1000

            print("帧数：" + str(round(fps, 2)) + " fps/s")

            self.frameCount = 0
            self.lastTime = self.now

            self.printCount += 1  # 记录打印次数


'''
zhenshu = Zhenshu()
isLoop = True

while isLoop:

    zhenshu.update()  # 测试1秒钟内执行多少次
    if zhenshu.printCount >= 4:  # 当打印次数大于4次时，结束性能测试
        isLoop = False
'''