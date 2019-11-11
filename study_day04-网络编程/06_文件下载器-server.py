"""
文件下载服务端

"""
import socket


def main():
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口和ip
    tcp_server_socket.bind(("", 8080))

    # 让socket设置为监听模式
    # 128表示多个客户端可以同时链接
    tcp_server_socket.listen(128)

    # 等待客户端链接
    new_clinet_socket, client_addr = tcp_server_socket.accept()

    # 接收客户端数据
    file_name = new_clinet_socket.recv(1024)
    print(file_name)

    # 响应数据给客户端
    new_clinet_socket.send("-----------ok--------".encode("utf-8"))

    # 关闭socket
    new_clinet_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
