class Yanchi:
    datetimeModule = None  # datetime模块
    urequestsModule = None  # urequests模块

    between = 0

    def __init__(self):
        # self.datetimeModule = __import__("datetime")
        self.datetimeModule = __import__("time")
        self.urequestsModule = __import__("urequests")

    def calibrate(self, apiUrl):
        try:
            response = self.urequestsModule.get(apiUrl)
            if response.status_code == 200:
                self.between = int(response.text)
                print(self.between)
            else:
                print('Error: ', response.status_code)
                print(response.text)  # 打印原始响应内容以进行调试
        finally:
            response.close()  # 确保关闭响应

    def get_timestamp(self):
        # return self.datetimeModule.datetime.now().timestamp() * 1000  # 将秒转成毫秒
        return self.datetimeModule.ticks_ms()

    def start(self):
        return self.get_timestamp() + self.between

    def end(self, date):
        delay = self.get_timestamp() + self.between - date
        print("延迟："+str(delay)+" ms | "+str(round(delay / 1000, 2))+" s")

'''
yc = Yanchi()
yc.calibrate('http://192.168.31.95:80/api/getTime?current=' + str(yc.get_timestamp()))
'''