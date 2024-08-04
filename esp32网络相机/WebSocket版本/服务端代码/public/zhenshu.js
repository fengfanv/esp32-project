function Zhenshu(dom) {
    this.dom = dom;

    this.lastTime = 0;
    this.now = 0;
    this.frameCount = 0;
    this.update = function () {
        this.now = performance.now(); //单位毫秒，比Date.now()更精确
        this.frameCount++; //记录1秒钟内被执行多次
        if (this.now - this.lastTime >= 1000) {
            //如果已经过去1秒，则计算每秒的帧数
            const fps = this.frameCount / (this.now - this.lastTime) * 1000;
            
            dom.innerText = `帧数：${Math.floor(fps)} fps/s`;

            this.frameCount = 0;
            this.lastTime = this.now;
        }
    }
}


// var zhenshu = new Zhenshu();

// function animation() {

//     zhenshu.update()

//     requestAnimationFrame(animation)
// }
// animation()