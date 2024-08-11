import camera
import time

# 初始化摄像头
try:
    camera.init(0, format=camera.JPEG)
except Exception as e:
    camera.deinit()  # 释放摄像头资源
    camera.init(0, format=camera.JPEG)

try:
    # 白平衡
    camera.whitebalance(1)
    
    # 拍摄一张照片
    buf = camera.capture()  # 大小是640x480
    print(type(buf)) # <class 'bytes'>
    print(len(buf)) # 7389字节 或 11865字节 或 15224字节 或 14498字节

    camera.deinit()  # 释放摄像头资源

    # 保存图片到文件
    imgName = "第一张照片"+str(time.time())+".jpg"
    with open(imgName, "wb") as f:
        f.write(buf)  # buf中的数据就是图片数据，所以直接写入到文件就行了
        print("拍照完成且保存成功！")

except KeyboardInterrupt:
    # 清理资源
    camera.deinit()
finally:
    # 清理资源
    camera.deinit()
