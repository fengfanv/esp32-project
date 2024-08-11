import select
import uwebsockets.client
import time

import redLed
import flashLamp
import device
import webCam


websocket = None
isPushVideo = False

def open_ws():
    global websocket, isPushVideo
    
    try:
        websocket = uwebsockets.client.connect("ws://192.168.31.95:3000/?user=esp32")
        # websocket.settimeout(0) # 为recv()设置一个超时，防止recv接收消息 阻塞 程序进程
        
        while True:
            # 接收消息
            reav_msg()
            
            '''
            # 发送消息
            msgTo = 'admin'.encode()
            msgFrom = 'esp32'.encode()
            msgType = 'messa'.encode()
            msgData = '1234567890'.encode()
            msg = msgTo + msgFrom + msgType + msgData
            # print(type(msg)) # <class 'bytes'>
            websocket.send(msg)
            time.sleep(1)
            '''
            
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
                websocket.send(msg)
            
    except:
        # 清理资源
        websocket.close()


def close_ws():
    global websocket
    
    try:
       websocket.close()
    except:
        pass

def reav_msg():
    global websocket, isPushVideo
    
    try:
        readable, _, _ = select.select([websocket.sock], [], [], 0)  # 0秒超时，非阻塞
        if websocket.sock in readable:
            resp = websocket.recv()
            msg = resp.decode()
            # 0-4表示去哪里
            # 5-9表示从哪来
            # 10-14表示消息类型（video、yanch、code_、等）
            # 15往后是数据本体
            msgTo = msg[0:5]
            msgFrom = msg[5:10]
            msgType = msg[10:15]
            msgData = msg[15:]
            
            if(msgType == 'code_'):
                if(msgData == 'open_redled'):
                    status = redLed.open()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='开启红LED成功'
                    else:
                        replyMsg+='开启红LED失败'
                    websocket.send(replyMsg.encode())
                elif(msgData == 'close_redled'):
                    status = redLed.close()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='关闭红LED成功'
                    else:
                        replyMsg+='关闭红LED失败'
                    websocket.send(replyMsg.encode())
                elif(msgData == 'open_flashlamp'):
                    status = flashLamp.open()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='开启闪光灯成功'
                    else:
                        replyMsg+='开启闪光灯失败'
                    websocket.send(replyMsg.encode())
                elif(msgData == 'close_flashlamp'):
                    status = flashLamp.close()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='关闭闪光灯成功'
                    else:
                        replyMsg+='关闭闪光灯失败'
                    websocket.send(replyMsg.encode())
                elif(msgData == 'get_temperature'):
                    temperature = device.temperature()
                    replyMsg = msgFrom+msgTo+'messa'+temperature
                    websocket.send(replyMsg.encode())
                elif(msgData == 'open_camera'):
                    status = webCam.open()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='开启相机成功'
                    else:
                        replyMsg+='开启相机失败'
                    websocket.send(replyMsg.encode())
                elif(msgData == 'close_camera'):
                    status = webCam.close()
                    replyMsg = msgFrom+msgTo+'messa'
                    if status:
                        replyMsg+='关闭相机成功'
                    else:
                        replyMsg+='关闭相机失败'
                    websocket.send(replyMsg.encode())
                    isPushVideo = False
                elif(msgData == 'get_image'):
                    imageData = webCam.getImg()
                    replyMsg = msgFrom+msgTo
                    replyMsg = replyMsg.encode()
                    if(isinstance(imageData,bytes)):
                        replyMsg += 'image'.encode()+imageData
                    else:
                        replyMsg += 'messa'.encode()+'获取照片失败'.encode()
                    websocket.send(replyMsg)
                elif(msgData == 'open_push'):
                    isPushVideo = True
                    replyMsg = msgFrom+msgTo
                    replyMsg = replyMsg.encode()
                    replyMsg += 'messa'.encode()+'esp32已收到开启推流的请求'.encode()
                    websocket.send(replyMsg)
                elif(msgData == 'close_push'):
                    isPushVideo = False
                    replyMsg = msgFrom+msgTo
                    replyMsg = replyMsg.encode()
                    replyMsg += 'messa'.encode()+'esp32已收到关闭推流的请求'.encode()
                    websocket.send(replyMsg)
            else:
                print(msgTo)
                print(msgFrom)
                print(msgType)
                print(msgData)
    except:
        pass

open_ws()

