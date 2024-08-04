function Yanchi(dom) {
    this.dom = dom;

    this.between = 0;
    this.calibrate = function (apiUrl) {

        //创建一个ajax实例
        let xhr = new XMLHttpRequest()

        //配置请求
        xhr.open('GET', apiUrl, false)

        //监听请求过程
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4 && xhr.status === 200) {

                console.log(xhr.responseText)
                this.between = Math.abs(xhr.responseText)

            }
        }

        //发送请求
        xhr.send()
    }

    this.start = function () {
        return Date.now() - this.between;
    }

    this.end = function (date) {
        const delay = Date.now() - this.between - date;
        this.dom.innerText = `延迟：${delay} ms | ${(delay / 1000).toFixed(2)} s`;
    }

}