def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Xiaomi_1042', 'xxx')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

# do_connect()