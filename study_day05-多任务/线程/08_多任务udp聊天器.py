"""
多线程的方式实现udp聊天器

"""
import threading
import socket


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)
        print(recv_data[0].decode("utf-8"))


def send_msg(udp_socket):
    while True:
        data = input("\n请输入发送的数据")
        udp_socket.sendto(data.encode("utf-8"), ("", 8080))


def main():
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("", 8080))

    # 创建两个线程
    thread1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    thread2 = threading.Thread(target=send_msg, args=(udp_socket,))

    # 接收消息
    thread1.start()
    # 发送消息
    thread2.start()


if __name__ == '__main__':
    main()


