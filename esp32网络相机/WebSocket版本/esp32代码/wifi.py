def do_connect():
    import network
    import time
    
    # 连接wifi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Xiaomi_1042', 'xxx')
    
        while not wlan.isconnected():
            print('正在连接wifi...')
            time.sleep(1)
    
    print('网络配置:', wlan.ifconfig())

do_connect()