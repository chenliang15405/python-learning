"""
while 循环语法：

while 条件:
    条件成立执行的代码
    ...

while循环嵌套

while 条件1:
    条件1执行的代码
    while 条件2:
        条件2成立执行的代码



循环的退出和终止：

break 和 continue

break: 终止此循环
continue： 退出当前循环进行下一次循环


循环和 else 配合使用
else 下方缩进的代码值的是当循环正常结束之后执行的代码
 注意：
    如果是break语句终止循环，那么 else中的代码不会执行
    continue 表示循环是正常结束，else中的代码会继续执行

while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码


"""

i = 1
result = 0

while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

print(f'偶数累加为：{result}')



j = 0
result2 = 0

while j <= 100:
    result2 += j
    j += 2

print("偶数累加方法2：结果为: %s" % result2)


'打印*号'
x = 0
while x < 5:
    y = 0
    while y < 5:
        print("*", end="")
        y += 1
    print(end="\n")
    x += 1


'打印三角形 *'

sanjiaox = 0

while sanjiaox < 6:
    sanjiaoxy = 0
    while sanjiaoxy < sanjiaox:
        print("*", end="")
        sanjiaoxy += 1
    print(end="\n")
    sanjiaox += 1