import camera

# 摄像头初始化
def init():
    try:
        camera.init(0, format=camera.JPEG)
    except Exception as e:
        camera.deinit()
        camera.init(0, format=camera.JPEG)

    # 摄像头翻转 上翻/下翻 0,1
    camera.flip(1)

    # 摄像头镜像 左/右 0,1
    camera.mirror(1)
    
    print('相机初始化成功')


def deinit():
    camera.deinit()


def getImg():
    return camera.capture()  # 获取图像数据
        
