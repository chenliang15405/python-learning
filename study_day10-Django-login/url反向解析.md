> url反向解析，服务端的url虽然改变，但是页面上的url是通过动态
>配置的，不需要也改变url


1. 在项目的urls中包含具体应用的urls文件时指定 namespace
 `url(r'^', include('booktest.urls'), namespace='booktest')`
 或者：
 - 使用path和re_path配置为：  
 `re_path(r'^', include(('booktest.urls', 'booktest'), namespace='booktest'))`

2. 在应用的urls文件中指定name   
`re_path(r'^showarg(\d+)$', views.show_arg, name='showarg'')`


3. 模版文件中使用指定的格式访问url即可，不需要配置固定的url路径
`{% url 'namespace名字:urls中name' %}`

带位置参数的格式：
`{% url 'namespace名字:urls中name' 参数 %}`
例如： `{% url 'namespace名字:urls中name' 1 %}`

或者：
`{% url 'namespace名字:urls中name' id=1 %}`


服务端重定向到动态的url

from django.core.urlresolvers import reverse

url = reverse('booktest:showarg')  # 配置的是 namespace:name
redirect(url)

带参数的动态url    
url = reverse('booktest:showarg', args=(1, 2)) 
redirect(url)

固定名称参数的动态url    
url = reverse('booktest:showarg', kwargs={'c'=3, 'd'=2}) 
redirect(url)
