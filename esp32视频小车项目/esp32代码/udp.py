import select
import socket
import time

import flashLamp
import steeringEngine
import car
import realTime


def udp_socket():
    try:
        # 创建upd 套接字（socket.AF_INET代表ipv4，socket.SOCK_DGRAM代表使用upd协议）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 设置此udp的网络信息
        addr = ('0.0.0.0', 39993)
        s.bind(addr)

        print('udp服务启动成功')

        # 初始化相机
        realTime.init()

        while True:
            # 实时发送摄像头画面
            buf = realTime.getImg()  # 获取图像数据
            s.sendto(buf, ('192.168.31.95', 39990))  # 向服务器发送图像数据
            time.sleep(0.1)  # 隔0.1秒发一次


            # 接收消息（非阻塞）
            readable, _, _ = select.select([s], [], [], 0)  # 0秒超时，非阻塞
            if s in readable:
                recv_data = s.recvfrom(1024)  # 这里1024表示每次接收数据的最大字节数

                # 打印接收到的消息
                value = recv_data[0].decode('utf-8')
                print('msg:', value, 'from:', recv_data[1])

                if value == 'get_ip':
                    s.sendto('1', (recv_data[1][0], recv_data[1][1]))
                elif value == 'to_0':
                    steeringEngine.toDeg(0)
                elif value == 'to_45':
                    steeringEngine.toDeg(45)
                elif value == 'to_90':
                    steeringEngine.toDeg(90)
                elif value == 'to_135':
                    steeringEngine.toDeg(135)
                elif value == 'to_180':
                    steeringEngine.toDeg(180)
                elif value == 'car_up_open':
                    car.car_up_open()
                elif value == 'car_up_close':
                    car.car_up_close()
                elif value == 'car_down_open':
                    car.car_down_open()
                elif value == 'car_down_close':
                    car.car_down_close()
                elif value == 'car_left_open':
                    car.car_left_open()
                elif value == 'car_left_close':
                    car.car_left_close()
                elif value == 'car_right_open':
                    car.car_right_open()
                elif value == 'car_right_close':
                    car.car_right_close()
                elif value == 'turn_on_light':
                    flashLamp.turnOn()
                elif value == 'turn_off_light':
                    flashLamp.turnOff()

    except KeyboardInterrupt:
        # 清理资源
        s.close()
        realTime.deinit()
    finally:
        # 清理资源
        s.close()
        realTime.deinit()

# udp_socket()
