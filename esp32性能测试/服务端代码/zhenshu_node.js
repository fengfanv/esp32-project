function Zhenshu() {
    this.printCount = 0; //打印次数（测试次数）

    this.lastTime = 0;
    this.now = 0;
    this.frameCount = 0;
    this.update = function () {
        this.now = performance.now(); //单位毫秒，比Date.now()更精确
        this.frameCount += 1; //记录1秒钟内被执行多次
        if (this.now - this.lastTime >= 1000) {
            //如果已经过去1秒，则计算每秒的帧数
            const fps = (this.frameCount / (this.now - this.lastTime)) * 1000;

            console.log(`帧数：${Math.floor(fps)} fps/s`);

            this.frameCount = 0;
            this.lastTime = this.now;

            this.printCount += 1  //记录打印次数
        }
    }
}
exports.Zhenshu = Zhenshu;

/*
var zhenshu = new Zhenshu();
var isLoop = true;
while (isLoop) {
    //Math.random()*(100-1)+1 生成1到100之间的随机浮点数
    let res = (Math.random() * (100 - 1) + 1) + (Math.random() * (100 - 1) + 1)
    zhenshu.update()  // 测试1秒钟内执行多少次
    if (zhenshu.printCount >= 4) { //当打印次数大于4次时，结束性能测试
        isLoop = false
    }
}
*/