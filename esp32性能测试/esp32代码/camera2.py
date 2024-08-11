import camera
import zhenshu

# 初始化摄像头
try:
    camera.init(0, format=camera.JPEG)
except Exception as e:
    camera.deinit()  # 释放摄像头资源
    camera.init(0, format=camera.JPEG)


zs = zhenshu.Zhenshu()
try:
    while True:
        buf = camera.capture()
        zs.update()

except KeyboardInterrupt:
    # 清理资源
    camera.deinit()
finally:
    # 清理资源
    camera.deinit()

