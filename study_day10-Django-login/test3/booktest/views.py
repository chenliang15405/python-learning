from django.shortcuts import render, redirect


# Create your views here.


# 登录装饰器
def login_require(view_func):
    """登录判断装饰器"""

    def wrapper(request, *args, **kwargs):
        if request.session.has_key("isLogin"):
            # 已登录
            return view_func(request, *args, **kwargs)
        else:
            # 未登录
            return redirect("/login")

    return wrapper


@login_require
def index(request):
    return render(request, "booktest/index.html", {})


@login_require
def show_arg(request, num):
    return render(request, "booktest/index.html", {"num": num})


def show_arg2(request, num):
    return render(request, "booktest/index.html", {"num": num})


def login(request):
    """用户登录"""
    pass

