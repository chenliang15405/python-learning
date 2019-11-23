### Djangdo中使用过Mysql数据库配置

1. 在setting.py中配置使用的数据库类型
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'py',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```

2. 安装依赖
 `pip install pymysql`
 
3. 在__init__.py中增加配置
```
import pymysql

pymysql.install_as_MySQLdb()
```

**注意：**
django的2。2版本使用mysql会提示mysql版本不可用
解决方案：
1. 降低django版本到2.1.4以下
2. 修改虚拟环境中的配置：    
    其中  11_env是虚拟环境的python环境   
    (1) 修改 `11_env/lib/python3.7/site-packages/django/db/backends/mysql/base.py`
    中35、36行注释掉
    (2) 还是继续报错，则修改`operations.py`中的
    ` query = query.decode(errors='replace')`
    为
    ` query = query.encode(errors='replace')`