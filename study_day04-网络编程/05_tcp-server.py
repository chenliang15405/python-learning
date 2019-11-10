"""
    TCP的服务器

"""
import socket


def main():

    # 创建socket
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip
    tcp_addr = ("127.0.0.1", 8080)
    tcp_server.bind(tcp_addr)

    # 设置tcp为被动链接，监听
    tcp_server.listen(128)

    # 等待客户端链接，返回一个接收客户端的socket 和客户端的地址信息
    client_socket, clientAddr = tcp_server.accept()
    # 这个client_socket是处理客户端请求的socket
    print(clientAddr)

    while True:
        # 处理客户端请求
        recv_data = client_socket.recv(1024)
        print(str(recv_data, "UTF-8")) # 可以通过这种方式编码
        print(recv_data.decode("UTF-8")) # 也可以通过decode编码

        if recv_data:
            # 发送数据
            client_socket.send("------ok--------".encode("utf-8"))
        else:
            break

    # 关闭该客户端的套接字
    client_socket.close()

    # 关闭tcp server socket
    tcp_server.close()


if __name__ == '__main__':
    main()

