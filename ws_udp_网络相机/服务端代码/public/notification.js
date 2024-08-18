function Notification() {
    this.dom = document.createElement('div');
    this.dom.setAttribute('id', 'notification_box');
    this.dom.setAttribute('style', `
        width:100%;
        height:50vh;
        overflow:auto;
        display:flex;
        flex-direction:column;
        background:#fafafa;
        border:1px solid #eaeefb;
        border-radius:4px;
        margin:25px;
        padding:18px 0px;
    `);
    document.body.appendChild(this.dom);
}

Notification.prototype.datetimeFormat = function (d) {
    var date = new Date(d);
    var Y = date.getFullYear();
    var M = date.getMonth() + 1;
    M = M < 10 ? '0' + M : M;
    var D = date.getDate() < 10 ? '0' + date.getDate() : date.getDate();
    var h = date.getHours() < 10 ? '0' + date.getHours() : date.getHours();
    var m = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes();
    var s = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds();
    return `${Y}-${M}-${D} ${h}:${m}:${s}`;
}

Notification.prototype.createMessage = function (from, text) {
    var childDom = document.createElement('div');
    childDom.setAttribute('style', `
        height:auto;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        margin:25px;
        padding:18px 0px;
        border:1px solid #dcdfe6;
        border-radius:4px;
    `);
    var dateDom = document.createElement('p');
    dateDom.setAttribute('style', `text-align:center;`);
    dateDom.innerText = this.datetimeFormat(Date.now())
    childDom.appendChild(dateDom)

    var fromDom = document.createElement('p');
    fromDom.setAttribute('style', `text-align:center;`);
    fromDom.innerText = '来自：' + from;
    childDom.appendChild(fromDom)

    var textDom = document.createElement('p');
    textDom.setAttribute('style', `text-align:center;`);
    textDom.innerText = text;
    childDom.appendChild(textDom)

    this.dom.appendChild(childDom)

    setTimeout(() => {
        this.dom.scrollTop = this.dom.scrollHeight; //滚动条滚动到底部
    })
}

Notification.prototype.createImage = function (from, imgUrl) {
    var childDom = document.createElement('div');
    childDom.setAttribute('style', `
        height:auto;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        margin:25px;
        padding:18px 0px;
        border:1px solid #dcdfe6;
        border-radius:4px;
    `);
    var dateDom = document.createElement('p');
    dateDom.setAttribute('style', `text-align:center;`);
    dateDom.innerText = this.datetimeFormat(Date.now())
    childDom.appendChild(dateDom)

    var fromDom = document.createElement('p');
    fromDom.setAttribute('style', `text-align:center;`);
    fromDom.innerText = '来自：' + from;
    childDom.appendChild(fromDom)

    var imgDom = document.createElement('img');
    imgDom.setAttribute('style', `width:50%;height:auto;`);
    imgDom.src = imgUrl;
    childDom.appendChild(imgDom)

    this.dom.appendChild(childDom)

    setTimeout(() => {
        this.dom.scrollTop = this.dom.scrollHeight; //滚动条滚动到底部
    }, 1000)
}

// var notification = new Notification()
// notification.createMessage('esp32', '初始化成功')
// notification.createMessage('esp32', '初始化成功')
// notification.createImage('esp32', location.href + '/haimianbaobao.png')