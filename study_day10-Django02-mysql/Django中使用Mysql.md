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