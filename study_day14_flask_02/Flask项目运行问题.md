# Flask项目运行问题

1. 在pycharm中直接右键运行app.py，项目可以正常运行，但是是pycharm帮你运行的flask项目，并不会运行
main函数中的东西，就是if判断是没有用的，所以需要通过命令运行`python app.py`或者在pycharm中将app.py
配置为普通的.py文件来运行即可