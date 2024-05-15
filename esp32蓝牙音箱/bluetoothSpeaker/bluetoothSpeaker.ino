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
