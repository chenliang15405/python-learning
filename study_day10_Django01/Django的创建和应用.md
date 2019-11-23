虚拟环境的安装：
    (1) 进入到项目目录： python3 -m venv 11_env   
    (2) 激活虚拟环境： source 11_env/bin/activate   
    (3) 关闭虚拟环境 直接关闭终端或者deactivate   

1. 安装Django依赖：
`pip install Django`

2. 创建Django项目：
`django-admin startproject 项目名称`

 项目目录说明：
  - manage.py 项目的管理文件
  - urls.py 路由配置
  - wsgi.py web服务器和web框架之间交互的wsgi协议的入口
  - settings.py 项目的配置文件

3. 创建Django项目中的应用（如果开发的项目需要多个模块，那么就会有多个应用床架在项目中）

   `python manage.py startapp 应用名称`
   
  应用目录说明：
    - views.py 定义视图函数
    - tests.py 写测试代码
    - models.py 数据库的配置, 设计和表对应的类
    - admin.py 后台管理的配置
    
    应用需要在项目的settings.py文件中注册
    
4. 启动django程序
在manage.py目录下，运行：
`python manage.py runserver`   
如果需要指定端口启动：
`python manage.py runserver 127.0.0.1:8001`   
