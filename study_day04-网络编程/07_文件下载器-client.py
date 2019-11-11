"""
文件下载客户端

"""
import socket


def main():
    # 创建socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    server_addr = ("", 8080)
    tcp_client_socket.connect(("127.0.0.1", 8080))

    # 输入下载的文件名
    download_file_name = input("输入需要下载的文件名")

    # 发送数据到服务器
    tcp_client_socket.send(download_file_name.encode("utf-8"))

    # 接收返回数据
    recv_data = tcp_client_socket.recv(1024*1024)

    # 保存数据到文件中
    with open("[新]" + download_file_name, "wb") as f:
        f.write(recv_data)

    # 关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    main()