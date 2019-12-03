### 虚拟环境
> 在创建django或者flask的时候，都会使用虚拟环境来创建爱你项目，
这个是因为虚拟环境会复制python的目录到另一个文件目录中，在虚拟环境中
安装的包不会污染真正的python

- `pip list` 查看安装的包
- `pip freeze` 也用来查看安装的包
- `pip freeze > requirements.txt` 将安装的包重定向到文件，可以用来在其他环境中安装依赖
- `pip install -r requirements.txt` 逐行安装文件中的依赖


### 安装虚拟环境
- `virtualenv --version` 查看是否安装了虚拟环境
- `sudo pip install virtualenv` 安装虚拟环境   
  `sudo pip install virtualenvwrapper`

- 安装虚拟环境之后，提示找不到`mkvirtualenv`命令，需要配置环境变量
```bash
# 1. 创建目录存放虚拟环境
mkdir $HOME/.virtualenvs
# 2. 打开~/.bashrc文件，添加环境变量，centos是bash_profile
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtulenvwrapper.sh
# 3. 运行
source ~/.bashrc

```
- 创建虚拟环境`mkvirtualenv flask_py`
- 进入虚拟环境`workon flask_py`
- 退出虚拟环境`deactivate flask_py`

### 安装flask
- 指定版本安装`pip install flask==0.10.1`
    - mac系统：`easy_install flask==0.10.1`
