"""
实现客户端浏览器访问服务端

"""
import socket


def service_client(new_clinet):
    """处理请求"""
    request = new_clinet.recv(1024)
    print(request)

    # 返回Http数据给浏览器
    response = "HTTP /1.1 200 OK \r\n"
    response += "\r\n"
    response += "hhhhhhhhh"

    new_clinet.send(response.encode("utf-8"))

    new_clinet.close()


def main():
    """用来完成整体控制"""
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_socket.bind(("", 8080))
    # 监听
    tcp_server_socket.listen(128)

    # 服务客户端d
    while True:
        # 堵塞模式
        new_client, client_addr = tcp_server_socket.accept()
        service_client(new_client)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()






