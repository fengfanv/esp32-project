import select
import uwebsockets.client
import zhenshu
import daikuan
import cam

def open_ws():
    
    try:
        websocket = uwebsockets.client.connect("ws://192.168.31.95:3000/?user=esp32")
        # websocket.settimeout(0) # 为recv()设置一个超时，防止recv接收消息 阻塞 程序进程
        
        cam.init()
        zs = zhenshu.Zhenshu()
        dk = daikuan.Daikuan()
        
        while True:
            # 接收消息
            readable, _, _ = select.select([websocket.sock], [], [], 0)  # 0秒超时，非阻塞
            if websocket.sock in readable:
                resp = websocket.recv()
                msg = resp.decode()
                print(msg)
            
            # 发送消息
            buf = cam.getImg()
            websocket.send(buf)
            zs.update()
            dk.update(len(buf))
            
    except KeyboardInterrupt:
        # 清理资源
        websocket.close()
        cam.deinit()
    finally:
        # 清理资源
        websocket.close()
        cam.deinit()

open_ws()


