### Requests模块

1. requests模块中解决编解码问题:
    response.content.decode() // 默认使用utf-8解码
    response.content.decode("gbk")
    response.text

2. 将cookie对象转换为字典   
`request.util.dict_from_cookiejar`
3. 请求SSL证书   
`response = requests.get(url, verify=False)`

4. 设置请求超时   
`response = requests.get(url. timeout=10)`

5. 判断是否请求成功   
`assert response.status_code = 200`

6. json使用注意点
- json中字符串都是双引号
    - 如果不是双引号，需要转换为正规json
        - eval:能实现简单字符串和python类型转换
        - replace: 把单引号替换为双引号

7. 关于json模块的使用
- `json.loads()` 把json字符串转换为python类型
- `json.dumps()` 把python类型转换为json字符串
    - str() 也可以将python类型转换为字符串，不过json.dumps()可以设置其他属性
    - json.dumps(ret, ensure_ascii=False, ident=4)
        - ensure_ascii 设置中文不编码，正常显示  
        - ident 设置输出时的缩进







 
    