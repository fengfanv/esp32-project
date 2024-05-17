# esp32蓝牙音箱

esp32 + arduino

# 项目描述

蓝牙 A2DP

# 实现步骤

1、arduino编辑器，左上角，点击“文件”，然后点击“新建项目”

2、创建完毕后，按键盘“ctrl+s”，将项目保存到电脑上

3、保存完毕后，将“如下代码”复制到你项目的“xxxx.ino”文件内

```c
#include "BluetoothA2DPSink.h"

BluetoothA2DPSink a2dp_sink;

void setup() {
  // put your setup code here, to run once:

  i2s_pin_config_t my_pin_config = {
    .mck_io_num = I2S_PIN_NO_CHANGE,
    .bck_io_num = 12,    //BCLK(sck)
    .ws_io_num = 13,     //LRC(ws)
    .data_out_num = 14,  //DIN(sd)
    .data_in_num = I2S_PIN_NO_CHANGE
  };
  a2dp_sink.set_pin_config(my_pin_config);
  a2dp_sink.start("王哥蓝牙耳机2");
}

void loop() {
  // put your main code here, to run repeatedly:
}
```

4、使用git把“如下开源项目”克隆到电脑上

```
git clone https://github.com/pschatzmann/ESP32-A2DP.git
```

5、克隆到电脑上后，把开源项目里“src”文件夹内的“所有文件”复制到 你项目的根目录下

6、复制完毕后，点击arduino编辑器左上角的“上传”按钮，将代码烧录到esp32

# 补充说明

将如下代码注释，可解决上传(烧录)代码时“config.h”文件报“warning警告”的问题

```c
// config.h

// ......

/*
#if __has_include("AudioTools.h")
#  define A2DP_I2S_AUDIOTOOLS 1
#else
#  warning "AudioTools library is not installed"
#endif
*/

// ......
```

# 项目硬件

1、esp32（esp-wroom-32）

2、max98357

3、喇叭（4Ω-8Ω）

4、杜邦线（母对母、公对公）

5、电源（5V 2A）

# 参考链接

[ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP)

[ESP32+Arduino之7行代码实现蓝牙音箱](https://blog.csdn.net/donghaodonghaodo/article/details/133635414)

[arduino+esp32实现esp32蓝牙音响](https://blog.csdn.net/qwwewq111/article/details/131712339)