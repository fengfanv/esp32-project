import uwebsockets.client
import select

websocket = None

def open():
    global websocket
    websocket = uwebsockets.client.connect("ws://192.168.31.95:3000/?user=esp32")
    # websocket.settimeout(0.1) # 为recv()设置一个超时，防止recv接收消息 阻塞 程序进程

def recv():
    global websocket
    readable, _, _ = select.select([websocket.sock], [], [], 0)  # 0秒超时，非阻塞
    if websocket.sock in readable:
        return websocket.recv()
    else:
        return None

def send(buf):
    global websocket
    websocket.send(buf)

def close():
    global websocket
    websocket.close()