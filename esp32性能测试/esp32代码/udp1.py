import select
import socket
import time
import zhenshu
import daikuan
import cam

def udp_socket():
    try:
        # 创建upd 套接字（socket.AF_INET代表ipv4，socket.SOCK_DGRAM代表使用upd协议）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 设置此udp的网络信息
        addr = ('0.0.0.0', 39993)
        s.bind(addr)

        print('udp服务启动成功')
        
        cam.init()
        zs = zhenshu.Zhenshu()
        dk = daikuan.Daikuan()

        while True:
            # 发送消息
            buf = cam.getImg()
            s.sendto(buf, ('192.168.31.95', 6789))
            zs.update()
            dk.update(len(buf))

            # 接收消息（非阻塞）
            readable, _, _ = select.select([s], [], [], 0)  # 0秒超时，非阻塞
            if s in readable:
                recv_data = s.recvfrom(1024)  # 这里1024表示每次接收数据的最大字节数
                # 打印接收到的消息
                value = recv_data[0].decode('utf-8')
                print('msg:', value, 'from:', recv_data[1])

    except KeyboardInterrupt:
        # 清理资源
        s.close()
        cam.deinit()
    finally:
        # 清理资源
        s.close()
        cam.deinit()

udp_socket()

