# Flask项目部署

1. 部署的容器： Gunicorn
- 使用gunicorn来作为flask的容器，启动过gunicorn，可以通过指定flask的入口来启动flask项目

- 使用步骤：
    - 安装flask `pip install gunicorn`
    - 启动gunicorn
    `gunicorn -w 4 -b 127.0.0.1:5000 --access-logfile ./logs/log main:app`
    - 说明：
        - -w 指定4个线程启动
        - -b 指定绑定的ip和端口
        - -access-logfile 指定日志文件
        - main:app  main为指定的文件名称，app指定的是Flask对象的实例

2. 启动的多个gunicorn容器的时候，可以通过Nginx实现负载均衡来访问多个gunicorn容器对应的flask项目
 