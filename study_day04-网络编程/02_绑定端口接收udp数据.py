"""
指定Ip和端口，接收socket的发送数据

udp在客户端和服务端都是需要绑定端口和Ip
tcp经过了3次握手和4次挥手，所以客户端不需要绑定端口和ip,服务端需要绑定
tcp是面向链接的通信，udp是面向无连接的通信

"""
import socket


def main():

    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息, 这里相当于注册时自己的信息到本地
    local_addr = ("", 8080)
    udp_socket.bind(local_addr)

    while True:
        # 接收udp数据
        data = udp_socket.recvfrom(1024)
        if not data:
            break

        # data 这个变量接收到的是一个元组 (接收到的数据，(发送方ip, port))
        # 接收发送数据
        recv_data = data[0] # 元组也是列表，所以可以直接取值
        #  接收发送的地址信息
        recv_addr = data[1]  

        # 解析数据
        print("%s : %s" % (str(recv_addr), recv_data.decode("UTF-8")))

    udp_socket.close()


if __name__ == "__main__":
    main()
