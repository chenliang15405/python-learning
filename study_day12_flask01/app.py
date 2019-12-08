from flask import Flask, current_app

# 创建flask的应用对象
# __name__ 表示当前模块名字
#  模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录、templates目录为模版目录
app = Flask(__name__,
            static_url_path="/python",  # 访问静态资源的url前缀，默认值是static
            static_folder="static",  # 静态资源的目录，默认就是static
            template_folder="templates"  # 模版文件的目录，默认是templates
            )

# 配置参数的使用方式
# 如果是在pycharm中开启debug，那么需要在启动的配置中设置flask_debug打钩
# 1. 使用配置文件设置参数
# app.config.from_pyfile("config.cfg")


# 2. 使用对象配置参数
class Config:
    DEBUG = True
    CUSTOMER = "python"


app.config.from_object(Config)

# 3. 直接操作config的字典对象
# app.config["DEBUG"] = True


# 通过装饰器定义路由
@app.route('/')
def hello_world():
    """定义的视图函数"""
    # 定义配置在配置类中，获取自定义的参数方式：

    # 1. 如果可以访问到全局app对象，可以直接从app中获取，因为app.config是一个字典
    # print(app.config.get("CUSTOMER"))

    # 2. 如果操作不到全局app对象，那么就从current_app中获取，需要从flask中导入，和使用app相同
    print(current_app.config.get("CUSTOMER"))

    return 'Hello World!'


if __name__ == '__main__':
    # 启动flask程序
    # 可以在run方法中传递参数，设置访问ip、port、debug开启参数，其他的参数配置还是需要上面说的方法配置
    app.run(host="0.0.0.0", port=5000, debug=True)
