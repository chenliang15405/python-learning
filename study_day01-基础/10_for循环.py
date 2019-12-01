"""
for 循环：
  语法:
for 临时变量 in 序列:
    循环执行代码

break、continue 退出和终止循环


循环和 else 配合使用

else 下方缩进的代码值的是当循环正常结束之后执行的代码
 注意：
    如果是break语句终止循环，那么 else中的代码不会执行
    continue 表示循环是正常结束，else中的代码会继续执行

语法：
for 临时变量 in 序列:
    循环代码
else:
    循环正常结束执行的代码

利用for循环快速给数组中添加数据：
[i for i in rang(3)]  -> [0, 1, 2]

加判断条件
[i fro i in rang(3 if i%2 == 0)] -> [0, 2]


多个重复输出
["a" for i in rang(3)] -> ['a', 'a', 'a']



"""