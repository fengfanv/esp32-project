function Daikuan(dom) {
    this.dom = dom;

    this.lastTime = 0;
    this.now = 0;
    this.sizeCount = 0;
    this.update = function (size) {
        this.now = performance.now(); //单位毫秒，比Date.now()更精确
        this.sizeCount += size; //记录1秒钟内，累计接收到的数据包大小
        if (this.now - this.lastTime >= 1000) {
            //如果已经过去1秒，则计算每秒能传输多少字节数据
            const speed = this.sizeCount / (this.now - this.lastTime) * 1000;
            dom.innerHTML = `
                <p>网速1：${Math.floor(speed)} Byte/s | ${Math.floor(speed / 1024)} KByte/s | ${(speed / 1024 / 1024).toFixed(2)} MByte/s</p>
                <p>网速2：${Math.floor(speed * 8)} bit/s | ${Math.floor(speed * 8 / 1024)} Kbit/s | ${(speed * 8 / 1024 / 1024).toFixed(2)} Mbit/s</p>
            `;
            this.sizeCount = 0;
            this.lastTime = this.now;
        }
    }
}