var http = require('http');
var fs = require('fs');
var url = require('url');
var path = require('path');
var nodejsWebsocket = require('nodejs-websocket');
var zhenshu = require('./zhenshu_node');
var daikuan = require('./daikuan_node');

var zs = new zhenshu.Zhenshu();
var dk = new daikuan.Daikuan();

//http服务
var public_path = path.join(__dirname, "public")    //web容器地址
http.createServer(function (request, response) {
    response.setHeader("Access-Control-Allow-Origin", "*")
    response.setHeader("Access-Control-Allow-Headers", "X-Requested-With")
    response.setHeader("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS")
    response.setHeader("Access-control-max-age", "1000")

    //处理CORS复杂请求的预检请求
    if (request.method === 'OPTIONS') {
        console.log('复杂请求的预检请求')
        response.writeHead(200, {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild, sessionToken ',
            'Access-Control-Allow-Methods': 'PUT, POST, GET, DELETE, OPTIONS'
        })
        response.end()
        return false
    }

    var pathname = url.parse(request.url).pathname
    var file_address = path.join(public_path, decodeURI(pathname))
    fs.stat(file_address, function (err, stat) {
        if (err) {
            if (pathname == '/api/getData' && request.method == 'GET') {
                //get案例
                console.log('/api/getData', 'get', request.headers, url.parse(request.url).query);
                response.writeHead(200, { 'Content-Type': 'application/json' })
                response.end(JSON.stringify({ 'a': 111, 'b': 222, 'method': 'get' }))
            } else if (pathname == '/api/postData' && request.method == 'POST') {
                //post案例
                let postData = '';
                request.on('data', function (chunk) {
                    postData += chunk;
                });
                request.on('end', function () {
                    console.log('/api/postData', 'post', request.headers, postData);
                });
                response.writeHead(200, { 'Content-Type': 'application/json' })
                response.end(JSON.stringify({ 'a': 111, 'b': 222, 'method': 'post' }))
            } else {
                response.writeHead(404, { 'Content-Type': 'text/plain;charset=utf-8' })
                response.end('状态：404，没有这样的文件或目录！')
            }
        } else {
            if (pathname == '/') {
                file_address = path.join(public_path, decodeURI('/index.html'))
                pathname = '/index.html'
            }
            var file_type = pathname.split('.')[1]
            var MIME = ''
            if (file_type == 'html' || file_type == 'htm') {
                MIME = 'text/html'
            } else if (file_type == 'css') {
                MIME = 'text/css'
            } else if (file_type == 'js') {
                MIME = 'text/javascript'
            } else if (file_type == 'png') {
                MIME = 'image/png'
            } else if (file_type == 'jpg' || file_type == 'jpeg') {
                MIME = 'image/jpeg'
            } else if (file_type == 'gif') {
                MIME = 'image/gif'
            }
            fs.readFile(file_address, function (err, fileData) {
                if (err) {
                    console.log(err)
                }
                response.writeHead(200, { 'Content-Type': MIME })
                response.end(fileData)
            })
        }
    })
}).listen(80, function () {
    console.log('http服务启动成功')
})

//--------------------------------------------------------------------------------------------------------------------------------------

//websocket服务
var wsServer = nodejsWebsocket.createServer((connection) => {
    //用户连接websocket服务，初始化用户信息
    var user = new URLSearchParams(connection.path.replace(/^[/|?]/g, '')).get('user')
    connection.user = user
    console.log(`用户 ${user} 连接websocket服务`)

    //监听客户端发来的text消息
    connection.on('text', (data) => {
        //console.log('text', data)
        wsRecv(data)
    })

    //监听客户端发来的binary消息
    connection.on('binary', (stream) => {
        var data = undefined; //Buffer 或 String
        stream.on('data', (chunk) => {
            if (data === undefined) {
                data = chunk;
                return false
            }
            if (Buffer.isBuffer(chunk)) {
                data = Buffer.concat([data, chunk], data.length + chunk.length)
            } else if (typeof chunk === 'string') {
                data += chunk;
            }
        })
        stream.on('end', () => {
            // console.log('binary', data)
            wsRecv(data)
        })
        stream.on('error', (err) => console.error('stream-err:', err.message))
    })


    //监听客户端关闭连接
    connection.on('close', (code, reason) => {
        console.log(`用户 ${connection.user} 连接关闭`)
    })
    //监听连接错误
    connection.on('error', (error) => {
        console.log(`用户 ${connection.user} 连接错误：`, error)
    })
})
wsServer.listen(3000, () => {
    console.log('websocket服务启动成功')
})

//ws接收消息
function wsRecv(data) {

    if (Buffer.isBuffer(data) == false) {
        data = Buffer.from(data);
    }

    let size = data.length;
    dk.update(size);
    zs.update();

    // //0-4表示去哪里
    // //5-9表示从哪来
    // //10-14表示消息类型（video、yanch、code_、等）
    // //15往后是数据本体
    // var to, from, type, body

    // if (Buffer.isBuffer(data)) {
    //     to = Buffer.alloc(5)
    //     from = Buffer.alloc(5)
    //     type = Buffer.alloc(5)
    //     body = Buffer.alloc(data.length - 15)
    //     data.copy(to, 0, 0, 5)
    //     data.copy(from, 0, 5, 10)
    //     data.copy(type, 0, 10, 15)
    //     data.copy(body, 0, 15, data.length)
    //     to = to.toString()
    //     from = from.toString()
    //     type = type.toString()
    //     body = body.toString()
    // } else if (typeof data === 'string') {
    //     to = data.slice(0, 5)
    //     from = data.slice(5, 10)
    //     type = data.slice(10, 15)
    //     body = data.slice(15)
    // }

    // // console.log(to)
    // // console.log(from)
    // // console.log(type)
    // // console.log(body)

    // //转发消息
    // wsSend(data, from, to)
}

//ws发送消息
function wsSend(msg, from, to) {
    if (typeof msg == 'undefined') {
        return false
    }
    if (typeof from == 'undefined') {
        //没有来源，则说明，这条消息是系统发的
        from = 'system'
    }
    if (typeof to == 'undefined') {
        //没有指定发给谁，则广播给所有用户
        to = 'all'
    }

    var send = Buffer.isBuffer(msg) ? 'sendBinary' : 'sendText'

    if (to == 'all') {
        //发给全部的人
        wsServer.connections.forEach((connection) => {
            connection[send](msg)
        })
    } else {
        //发给指定的人
        wsServer.connections.forEach((connection) => {
            if (connection.user == to) {
                connection[send](msg)
            }
        })
    }
}