> Django中的orm可以通过定义在应用文件中的实体配置属性，然后通过命令自动生成迁移文件，通过迁移文件创建表

数据库的配置在setting.py文件中，默认使用sqlite3, 可以通过sqliteman打开软件，然后查看该文件即可

1. 定义数据表的模型类 

2. 生成迁移文件，在项目的根目录执行，因为都是通过manage.py执行
`python manage.py makemigrations`

3. 生成迁移文件之后，创建数据表
`python manage.py migrate`

生成的表明的默认格式： 
    应用名_模型类名小写
    


关系操作  

由一查多：  
b.heroinfo_set.all()

由多查一：  
h.hbook

如果保存多的时候，需要给多中的关系属性赋值 一的类的对象，而不是id


查询一个表的所有数据
HeroInfo.objects.all()