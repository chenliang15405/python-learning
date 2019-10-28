"""
递归

"""

def sum_num(num):
    print(num)

    if num == 1:
        return

    sum_num(num - 1)

sum_num(6)



# 累加的递归
def sum_numbers(num):

    if num == 1:
        return 1

    # 倒序的相加，然后利用最后一位数是1来返回一个确定的值以及递归的退出条件
    return num + sum_numbers(num - 1)


result = sum_numbers(100)
print(result)

