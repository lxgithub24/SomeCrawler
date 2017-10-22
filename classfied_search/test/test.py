# -*- coding:utf-8 -*-
import json
import random, time
import codecs
import urlparse
from classfied_search.model import ORM


def get_dict():
    res = ORM.College_info.query(2)
    info = res.info
    info = json.dumps(info, encoding='utf8', ensure_ascii=False)
    print info
    f = codecs.open('tmp', 'w', 'utf8')
    f.write(info)


def python_select():
    import select
    import socket
    import sys

    HOST = 'localhost'
    PORT = 5000
    BUFFER_SIZE = 1024

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    inputs = [server, sys.stdin]
    running = True

    while True:
        try:
            # 调用 select 函数，阻塞等待
            readable, writeable, exceptional = select.select(inputs, [], [])
        except select.error, e:
            break

        # 数据抵达，循环
        for sock in readable:
            # 建立连接
            if sock == server:
                conn, addr = server.accept()
                # select 监听的socket
                inputs.append(conn)
            elif sock == sys.stdin:
                junk = sys.stdin.readlines()
                running = False
            else:
                try:
                    # 读取客户端连接发送的数据
                    data = sock.recv(BUFFER_SIZE)
                    if data:
                        sock.send(data)
                        if data.endswith('\r\n\r\n'):
                            # 移除select监听的socket
                            inputs.remove(sock)
                            sock.close()
                    else:
                        # 移除select监听的socket
                        inputs.remove(sock)
                        sock.close()
                except socket.error, e:
                    inputs.remove(sock)

    server.close()


def python_epoll():
    import socket
    import select

    EOL1 = b'\n\n'
    EOL2 = b'\n\r\n'
    response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
    response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
    response += b'Hello, world!'

    # 创建套接字对象并绑定监听端口
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('0.0.0.0', 8080))
    serversocket.listen(1)
    serversocket.setblocking(0)

    # 创建epoll对象，并注册socket对象的 epoll可读事件
    epoll = select.epoll()
    epoll.register(serversocket.fileno(), select.EPOLLIN)

    try:
        connections = {}
        requests = {}
        responses = {}
        while True:
            # 主循环，epoll的系统调用，一旦有网络IO事件发生，poll调用返回。这是和select系统调用的关键区别
            events = epoll.poll(1)
            # 通过事件通知获得监听的文件描述符，进而处理
            for fileno, event in events:
                # 注册监听的socket对象可读，获取连接，并注册连接的可读事件
                if fileno == serversocket.fileno():
                    connection, address = serversocket.accept()
                    connection.setblocking(0)
                    epoll.register(connection.fileno(), select.EPOLLIN)
                    connections[connection.fileno()] = connection
                    requests[connection.fileno()] = b''
                    responses[connection.fileno()] = response
                elif event & select.EPOLLIN:
                    # 连接对象可读，处理客户端发生的信息，并注册连接对象可写
                    requests[fileno] += connections[fileno].recv(1024)
                    if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                        epoll.modify(fileno, select.EPOLLOUT)
                        print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
                elif event & select.EPOLLOUT:
                    # 连接对象可写事件发生，发送数据到客户端
                    byteswritten = connections[fileno].send(responses[fileno])
                    responses[fileno] = responses[fileno][byteswritten:]
                    if len(responses[fileno]) == 0:
                        epoll.modify(fileno, 0)
                        connections[fileno].shutdown(socket.SHUT_RDWR)
                elif event & select.EPOLLHUP:
                    epoll.unregister(fileno)
                    connections[fileno].close()
                    del connections[fileno]
    finally:
        epoll.unregister(serversocket.fileno())
        epoll.close()
        serversocket.close()


if __name__ == '__main__':
    # python_select()
    python_epoll()