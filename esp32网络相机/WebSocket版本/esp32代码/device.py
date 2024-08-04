def temperature():
    import esp32
    return str(esp32.raw_temperature())+'°F' # 获取MCU温度，单位华氏度