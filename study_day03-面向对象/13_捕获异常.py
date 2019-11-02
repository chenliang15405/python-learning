"""
捕获异常：出现异常进行处理，并继续执行try 下面的代码
    语法：
        try:
            尝试执行的代码
        except:
            出现错误的处理



错误类型捕获异常：
    根据不同类型的异常，进行不同的捕获和处理
    报错时，最后一行的第一个单词就是异常类型

    语法：
        try
            pass
        except 错误类型1:
            pass
        except (错误类型2， 错误类型3)
            pass
        except Exception as result:
            print("未知错误%s" % result)


最后一个可以捕获未知错误，进行处理



异常捕获完整语法：
     try
        pass
     except 错误类型1:
        pass
     except (错误类型2， 错误类型3)
        pass
     except Exception as result:
        # 打印错误信息
        print(result)
     else:
        # 没有异常执行的代码 
        pass
     finally:
        # 无论是否有异常，都会执行的代码
        print("finally 执行")













"""

try:
    num = int(input("请输入一个整数"))
except ValueError:
    print("异常")
except Exception as result:
    print("未知错误%s" % result)


