

def num_div(num1, num2):
    # 使用assert 来进行断言
    assert isinstance(num1, int)
    assert isinstance(num2, int)

    print(num1/ num2)


if __name__ == '__main__':
    num_div(10, 1)
    num_div('10', '2')

