function Daikuan() {
    this.printCount = 0;

    this.lastTime = 0;
    this.now = 0;
    this.sizeCount = 0;
    this.update = function (size) {
        this.now = performance.now(); //单位毫秒，比Date.now()更精确
        this.sizeCount += size; //记录1秒钟内，累计接收到的数据包大小
        if (this.now - this.lastTime >= 1000) {
            //如果已经过去1秒，则计算每秒能传输多少字节数据
            const speed = (this.sizeCount / (this.now - this.lastTime)) * 1000;

            //清除控制台
            // console.clear();

            console.log(`网速1：${Math.floor(speed)} Byte/s | ${Math.floor(speed / 1024)} KByte/s | ${(speed / 1024 / 1024).toFixed(2)} MByte/s`);
            console.log(`网速2：${Math.floor(speed * 8)} bit/s | ${Math.floor(speed * 8 / 1024)} Kbit/s | ${(speed * 8 / 1024 / 1024).toFixed(2)} Mbit/s`);

            this.sizeCount = 0;
            this.lastTime = this.now;

            this.printCount++;
        }
    }
}
exports.Daikuan = Daikuan;

/*
var daikuan = new Daikuan();
var chunk = Buffer.alloc(1); //申请1字节的内存空间
var isLoop = true;
while (isLoop) {
    daikuan.update(chunk.length)  // 记录一秒内能累计接收多少字节的数据
    if (daikuan.printCount >= 10) { //当打印次数大于10次时，结束性能测试
        isLoop = false
    }
}
*/