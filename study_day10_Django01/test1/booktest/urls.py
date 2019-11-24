# from django.conf.urls import url
from django.urls import path
from booktest import views

urlpatterns = [
    # 通过url函数设置url的路由配置
    # url(r"^index", views.index) # 建立/index和视图之间的关系
    path("index", views.index),  # django2.2之后创建的项目使用的是这个
    path("index2", views.index2),
    path("books", views.books),
    path("books/<bid>", views.book_detail)
]
