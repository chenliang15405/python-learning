"""
实现客户端浏览器访问服务端的文件

"""
import socket
import re


def service_client(new_clinet):
    """处理请求"""
    # 以utf-8编码对字符串str进行解码，获得字符串类型对象
    request = new_clinet.recv(1024).decode("utf-8")
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
    response += "\r\n"

    try:
       f = open("./html" + file_name, "rb")
    except:

        # 发送header给浏览器，并返回body给浏览器
        # 以utf-8编码对u进行编码，获得bytes类型对象
        new_clinet.send(response.encode("utf-8"))
        # 需要返回二进制，读取的就是二进制文件
        new_clinet.send("-------file not found------".encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 发送header给浏览器，并返回body给浏览器
        # 以utf-8编码对u进行编码，获得bytes类型对象
        new_clinet.send(response.encode("utf-8"))
        # 需要返回二进制，读取的就是二进制文件
        new_clinet.send(html_content)

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






