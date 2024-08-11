var dgram = require('dgram');
var zhenshu = require('./zhenshu_node');
var daikuan = require('./daikuan_node');

var zs = new zhenshu.Zhenshu();
var dk = new daikuan.Daikuan();

//udp接收数据案例

//创建udp
var udp = dgram.createSocket('udp4');
//给此udp绑定端口号。不绑定端口号，程序在运行时，系统会为其分配一个临时随机端口号
udp.bind(6789);

//监听端口
udp.on('listening', function () {
    console.log('udp server linstening 6789');
})

//接收消息
udp.on('message', function (msg, rinfo) {

    if (Buffer.isBuffer(msg) == false) {
        msg = Buffer.from(msg)
    }
    let size = msg.length;
    dk.update(size);
    zs.update();

    // msgStr = msg.toString();
    // console.log(`udp server received data: ${msgStr} from ${rinfo.address}:${rinfo.port}`)
})

//错误处理
udp.on('error', function (err) {
    console.log('some error on udp server')
    udp.close();
})