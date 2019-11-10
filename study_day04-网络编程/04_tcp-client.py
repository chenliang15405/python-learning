"""
TCP 客户端

"""
import socket


def main():

    # 创建socket对象
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器, 传入的是一个元组,ip 为字符串， port 为number
    tcp_addr = ("127.0.0.1", 8080)
    tcp_socket.connect(tcp_addr)

    # 发送数据
    tcp_socket.send("这是一个数据".encode("UTF-8"))

    # 关闭链接
    tcp_socket.close()


if __name__ == '__main__':
    main()

