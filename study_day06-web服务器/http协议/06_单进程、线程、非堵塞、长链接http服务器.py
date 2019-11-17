"""
实现客户端浏览器访问服务端的文件

"""
import socket
import re


def service_client(new_clinet, request):
    """处理请求"""
    # 以utf-8编码对字符串str进行解码，获得字符串类型对象
    # request = new_clinet.recv(1024).decode("utf-8")
    # print(request)

    # 获取客户端的数据
    request_arr = request.splitlines()
    print(request_arr)

    # 根据正则匹配到请求的文件名和路径
    # GET /index.html HTTP/1.1
    # [^] ^在中括号中表示匹配非后面的字符
    ret = re.match(r"[^/]+(/[^ ]*)", request_arr[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 返回http格式数据给浏览器

    response = "HTTP /1.1 200 OK \r\n"

    try:
       f = open("./html" + file_name, "rb")
    except:

        # 发送header给浏览器，并返回body给浏览器
        # 以utf-8编码对u进行编码，获得bytes类型对象
        response += "\r\n"
        new_clinet.send(response.encode("utf-8"))
        # 需要返回二进制，读取的就是二进制文件
        new_clinet.send("-------file not found------".encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        # 通过设置content-length 来设置一次链接的结束，但是http的长链接是没有结束的，只是一次返回数据到客户端，否则会一直在加载
        response += "Content-Length:%d\r\n" % len(html_content)
        response += "\r\n"

        # 发送header给浏览器，并返回body给浏览器
        # 以utf-8编码对u进行编码，获得bytes类型对象
        new_clinet.send(response.encode("utf-8"))
        # 需要返回二进制，读取的就是二进制文件
        new_clinet.send(html_content)

    # 因为是长链接，所以就不需要关闭链接，设置content-length就会直接返回一次链接的数据
    # new_clinet.close()


def main():
    """用来完成整体控制"""
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_socket.bind(("", 8080))
    # 监听
    tcp_server_socket.listen(128)

    # 设置tcp_client为非堵塞模式，就不用堵塞在accept，可以接收多个client,但是会产生后面无法使用返回的对象，所以需要try
    tcp_server_socket.setblocking(False)

    # 创建集合用来放所有创建来的新客户端链接
    client_socket_list = list()

    # 服务客户端d
    while True:
        # 堵塞模式
        try:
            new_client, client_addr = tcp_server_socket.accept()
        except Exception as result:
            pass
        else:
            # 设置创建的指定的客户端socket也为非堵塞模式，防止在recv的时候堵塞
            new_client.setblocking(False)
            client_socket_list.append(new_client)

        # 遍历list,用来处理所有的客户端链接的数据
        for client_socket in client_socket_list:
            try:
                # 接收的是二进制，需要解码
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    # 为这个客户端服务
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    tcp_server_socket.close()


if __name__ == '__main__':
    main()


