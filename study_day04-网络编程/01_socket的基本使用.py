"""
socket的基本使用

    运行一个python程序: python3 xxx.py

"""
import socket


def main():

    # 创建socket
    # 第一个参数表示Ipv4，第二个参数表示是UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用套接字发送数据,发送的需要使用字节
    # 并且第二个参数接收一个元组，(ip, port)
    udp_socket.sendto(b"123312", ("127.0.0.1", 8080))

    # 关闭套接字
    udp_socket.close()


"""设置中文以UTF-8格式发送数据"""
def encode_main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以绑定发送者的端口，如果不绑定则随机分配
    udp_socket.bind(("", 7890))

    input_data = input("请输入内容：")

    udp_socket.sendto(input_data.encode("UTF-8"), ("127.0.0.1", 8080))

    udp_socket.close()


if __name__ == "__main__":
    # main()
    encode_main()
