import socket

udpServer = None

def open():
    global udpServer
    
    # 创建upd 套接字（socket.AF_INET代表ipv4，socket.SOCK_DGRAM代表使用upd协议）
    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 设置此udp的网络信息
    addr = ('0.0.0.0', 39993)
    udpServer.bind(addr)
    print('udp服务启动成功')

def close():
    global udpServer
    udpServer.close()

def send(buf):
    global udpServer
    udpServer.sendto(buf,('192.168.31.95', 39990))  # 向服务器发送图像数据
