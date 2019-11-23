from django.urls import path, re_path
from booktest import views

urlpatterns = [
    re_path(r'^index$', views.index),
    re_path(r'^showarg(\d+)$', views.show_arg),  # 通过位置参数捕获参数, 这样的参数，在函数中的参数变是任意定义
    path('arg/<num>', views.show_arg2, name='arg')  # 关键字参数，函数的参数接收必须和url中定义的名称一致，例如num
]
