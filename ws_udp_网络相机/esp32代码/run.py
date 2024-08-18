import redLed
import flashLamp
import device
import webCam
import yanchi

import udp
import ws

isPushVideo = False

def reav_msg():
    global isPushVideo

    resp = ws.recv()
    if resp:
        msg = resp.decode()
        # 0-4表示去哪里
        # 5-9表示从哪来
        # 10-14表示消息类型（video、yanch、code_、等）
        # 15往后是数据本体
        msgTo = msg[0:5]
        msgFrom = msg[5:10]
        msgType = msg[10:15]
        msgData = msg[15:]
        
        if (msgType == 'code_'):
            if (msgData == 'open_redled'):
                status = redLed.open()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '开启红LED成功'
                else:
                    replyMsg += '开启红LED失败'
                ws.send(replyMsg.encode())
            elif (msgData == 'close_redled'):
                status = redLed.close()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '关闭红LED成功'
                else:
                    replyMsg += '关闭红LED失败'
                ws.send(replyMsg.encode())
            elif (msgData == 'open_flashlamp'):
                status = flashLamp.open()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '开启闪光灯成功'
                else:
                    replyMsg += '开启闪光灯失败'
                ws.send(replyMsg.encode())
            elif (msgData == 'close_flashlamp'):
                status = flashLamp.close()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '关闭闪光灯成功'
                else:
                    replyMsg += '关闭闪光灯失败'
                ws.send(replyMsg.encode())
            elif (msgData == 'get_temperature'):
                temperature = device.temperature()
                replyMsg = msgFrom+msgTo+'messa'+temperature
                ws.send(replyMsg.encode())
            elif (msgData == 'open_camera'):
                status = webCam.open()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '开启相机成功'
                else:
                    replyMsg += '开启相机失败'
                ws.send(replyMsg.encode())
            elif (msgData == 'close_camera'):
                status = webCam.close()
                replyMsg = msgFrom+msgTo+'messa'
                if status:
                    replyMsg += '关闭相机成功'
                else:
                    replyMsg += '关闭相机失败'
                ws.send(replyMsg.encode())
                isPushVideo = False
            elif (msgData == 'get_image'):
                imageData = webCam.getImg()
                replyMsg = msgFrom+msgTo
                replyMsg = replyMsg.encode()
                if (isinstance(imageData, bytes)):
                    replyMsg += 'image'.encode()+imageData
                else:
                    replyMsg += 'messa'.encode()+'获取照片失败'.encode()
                ws.send(replyMsg)
            elif (msgData == 'open_push'):
                isPushVideo = True
                replyMsg = msgFrom+msgTo
                replyMsg = replyMsg.encode()
                replyMsg += 'messa'.encode()+'esp32已收到开启推流的请求'.encode()
                ws.send(replyMsg)
            elif (msgData == 'close_push'):
                isPushVideo = False
                replyMsg = msgFrom+msgTo
                replyMsg = replyMsg.encode()
                replyMsg += 'messa'.encode()+'esp32已收到关闭推流的请求'.encode()
                ws.send(replyMsg)
            elif (msgData == 'get_yanchi'):
                replyMsg = msgFrom+msgTo
                replyMsg = replyMsg.encode()
                replyMsg += 'yanch'.encode()
                replyMsg += str(yc.start()).encode()
                ws.send(replyMsg)
                
        elif (msgType == 'yanch'):
            
            yc.end(int(msgData))
            
        else:
            print(msgTo)
            print(msgFrom)
            print(msgType)
            print(msgData)


try:
    udp.open() # 启动udp服务
    ws.open() # 启动ws服务
    yc = yanchi.Yanchi()
    yc.calibrate('http://192.168.31.95:80/api/getTime?current='+str(yc.get_timestamp()))
    
    while True:
        # 接收消息
        reav_msg()
        
        # 发送视频数据
        if isPushVideo:
            imageData = webCam.getImg()
            msgTo = 'admin'
            msgFrom = 'esp32'
            msgType = 'video'
            msg = msgTo+msgFrom+msgType
            msg  = msg.encode()
            if(isinstance(imageData,bytes)):
                msg += imageData
            else:
                msg += str(imageData).encode()
            udp.send(msg)
        

except KeyboardInterrupt:
    # 清理资源
    udp.close()
    ws.close()
    webCam.close()
finally:
    # 清理资源
    udp.close()
    ws.close()
    webCam.close()
    

