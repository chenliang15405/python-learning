"""
实现客户端浏览器访问服务端的文件

"""
import multiprocessing
import re
import socket
import sys


class WSGLServer(object):

    def __init__(self, port, app, static_path):
        # 创建socket
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定端口
        self.tcp_server_socket.bind(("", port))
        # 监听
        self.tcp_server_socket.listen(128)

        self.headers = ""
        self.status = ""

        self.application = app
        self.static_path = static_path

    def service_client(self, new_clinet):
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

        if not file_name.endswith(".html"):
            try:
                f = open(self.static_path + file_name, "rb")
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
        else:
            # 通过调用服务器端框架，动态获取信息
            # WSGI 协议， 调用服务器的第一个参数需要是字典，第二个是函数
            env = dict()
            env["PATH_INFO"] = file_name

            try:
                body = self.application(env, self.start_response)
            except Exception as err:
                body = "-------file not found------"

            header = "HTTP /1.1 %s \r\n" % self.status
            for item in self.headers:
                header += "%s: %s\r\n" % (item[0], item[1])

            header += "\r\n"

            resp = header + body
            new_clinet.send(resp.encode("utf-8"))

        new_clinet.close()

    def start_response(self, status, header):
        self.status = status
        self.headers = header

    def run_forever(self):
        """用来完成整体控制"""
        # 服务客户端d
        while True:
            # 堵塞模式
            new_client, client_addr = self.tcp_server_socket.accept()

            # 使用多进程方式实现服务
            p = multiprocessing.Process(target=self.service_client, args=(new_client,))
            p.start()

            new_client.close()

        self.tcp_server_socket.close()


def read_conf():
    """读取配置文件"""
    with open("./web_server.conf", 'r', encoding="UTF-8") as f:
        # 使用eval函数将配置文件中的字符串转换为字典
        return eval(f.read())


def main():
    # 通过sys模块获取运行指定参数, 第一个参数是运行的文件，第二个是指定的port 第三个执行运行的web框架和方法
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as err:
            print("端口输入错误")
            return
    else:
        print("sys.argv")
        print("请按照以下方式运行： python3 xxx.py [port] [frame_name]:[app_name]")
        return

    # 获取启动的web框架名称和函数名称
    print(frame_app_name)
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print("re.match")
        print("请按照以下方式运行： python3 xxx.py [port] [frame_name]:[app_name]")
        return

    # 读取配置文件中定义的数据
    conf_content = read_conf()

    # 动态导入web框架
    # 需要加上模块的包名
    sys.path.append(conf_content["dynamic_path"])
    frame = __import__(frame_name)  # 动态导入的返回对象，表示这个模版
    app = getattr(frame, app_name)  # 此时app就指向了mini_frame框架中的application函数

    print(app)
    wsglServer = WSGLServer(port, app, conf_content["static_path"])
    wsglServer.run_forever()


if __name__ == '__main__':
    main()






