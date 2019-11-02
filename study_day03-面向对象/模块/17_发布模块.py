"""
可以发布模块给其他人使用：

制作发布包的步骤：
    1. 在包名的同级目录创建setup.py

    from distutils.core import setup

    setup(name="", # 包名
         version="1.0", #版本
         description="描述信息",
         long_description="完整的描述信息",
         author="作者",
         author_email="作者邮箱",
         url="主页"，
         py_modules=["包名.模块名1","包名.模块名2"]
    )

    2. 构建模块
    python3 setup.py build
    3. 生成发布压缩包
    python3 setup.py sdist


安装制作的python压缩包：
 安装模块
     tar -zxvf xxx.tar.gz
     sudo python3 setup.py install

   安装之后，就相当于在python3的lib中安装了这个依赖，项目中可以直接import 使用

 卸载模块：
    在安装目录下(可以使用__file__查看模块的安装目录)，删除该模块
    1. cd 安装模块
    2. sudo rm -rf 包名


"""