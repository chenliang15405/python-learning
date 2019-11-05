"""
使用socket实现udp聊天器

    udp 协议相对来说会丢包，所以不是非常安全

"""
import socket


def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("请输入发送的IP：")
    dest_port = int(input("请输入发送的Port："))
    input_data = input("请输入发送的消息：")

    udp_socket.sendto(input_data.encode("UTF-8"), (dest_ip, dest_port))


def receive_msg(udp_socket):
    """接收消息"""
    reve_data = udp_socket.recvfrom(1024)
    print("%s : %s" % (str(reve_data[1]), reve_data[0].decode("UTF-8")))


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 7788))

    while True:
        send_msg(udp_socket)

        receive_msg(udp_socket)


if __name__ == "__main__":
    main()

