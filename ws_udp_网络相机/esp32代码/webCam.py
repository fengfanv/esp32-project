import camera

def open():
    try:
        # 摄像头初始化
        try:
            camera.init(0, format=camera.JPEG)
        except Exception as e:
            camera.deinit()
            camera.init(0, format=camera.JPEG)
        
        # camera.JPEG -- 3
        # camera.GRAYSCALE -- 2
        # camera.YUV422 -- 1
        # camera.RGB565 -- 0
        
        # 摄像头翻转 上翻/下翻 0,1
        camera.flip(1)
        
        # 摄像头镜像 左/右 0,1
        camera.mirror(1)
        
        # 分辨率
        camera.framesize(camera.FRAME_VGA)
        # 选项如下：
        # FRAME_96X96 - 96x96 像素
        # FRAME_QQVGA - 160x120 像素 (QQVGA代表Quarter Quarter VGA)
        # FRAME_QCIF - 176x144 像素 (QCIF代表Quarter CIF)
        # FRAME_HQVGA - 240x160 像素 (HQVGA代表Half Quarter VGA)
        # FRAME_240X240 - 240x240 像素
        # FRAME_QVGA - 320x240 像素 (QVGA代表Quarter VGA)
        # FRAME_CIF - 352x288 像素 (CIF代表Common Intermediate Format)
        # FRAME_HVGA - 480x320 像素 (HVGA代表Half VGA)
        # FRAME_VGA - 640x480 像素 (VGA代表Video Graphics Array)
        # FRAME_SVGA - 800x600 像素 (SVGA代表Super VGA)
        # FRAME_XGA - 1024x768 像素 (XGA代表Extended Graphics Array)
        # FRAME_HD - 1280x720 像素 (HD代表High Definition)
        # FRAME_SXGA - 1280x1024 像素 (SXGA代表Super XGA)
        # FRAME_UXGA - 1600x1200 像素 (UXGA代表Ultra XGA)
        # FRAME_FHD - 1920x1080 像素 (FHD代表Full High Definition)
        # FRAME_P_HD - 1600x1200 像素 (P_HD代表Partial High Definition)
        # FRAME_P_3MP - 2048x1536 像素 (P_3MP代表Partial 3 Megapixels)
        # FRAME_QXGA - 2048x1536 像素 (QXGA代表Quad Extended Graphics Array)
        # FRAME_QHD - 2560x1440 像素 (QHD代表Quad High Definition)
        # FRAME_WQXGA - 2560x1600 像素 (WQXGA代表Wide Quad Extended Graphics Array)
        # FRAME_P_FHD - 2560x1600 像素 (P_FHD代表Partial Full High Definition)
        # FRAME_QSXGA - 2560x2048 像素 (QSXGA代表Quad Super XGA)
        
        # 特效(滤镜)
        camera.speffect(camera.EFFECT_NONE)
        # 选项如下：
        # EFFECT_NONE -- 0 无效果（默认）
        # EFFECT_NEG -- 1 负片效果
        # EFFECT_BW -- 2 黑白效果
        # EFFECT_RED -- 3 红色效果
        # EFFECT_GREEN -- 4 绿色效果
        # EFFECT_BLUE -- 5 蓝色效果
        # EFFECT_RETRO -- 6 复古效果
        
        # 白平衡
        camera.whitebalance(camera.WB_NONE)
        # 选项如下：
        # WB_NONE -- 0 无/自动白平衡
        # WB_SUNNY -- 1 晴天/日光白平衡
        # WB_CLOUDY -- 2 多云/阴天白平衡
        # WB_OFFICE -- 3 办公室/室内白平衡/荧光灯白平衡
        # WB_HOME -- 4 家庭/室内白平衡/白炽灯白平衡
        
        # 饱和度
        camera.saturation(0)
        # -2至2（默认为0）    -2灰度
        
        # 亮度
        camera.brightness(0)
        # -2至2（默认为0）    2明亮
    
        # 对比度
        camera.contrast(0)
        # -2至2（默认为0）    2高对比度
    
        # 质量
        camera.quality(63)
        # 10-63 数字越小质量越高
    
        return True
    except:
        return False

def getImg():
    try:
        return camera.capture()  # 获取图像数据
    except:
        return None

def close():
    try:
        camera.deinit()
        return True
    except:
        camera.deinit()
        return True
