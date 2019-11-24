# from django.conf.urls import url
from django.urls import path
from booktest import views

urlpatterns = [
    # 通过url函数设置url的路由配置
    # url(r"^index", views.index) # 建立/index和视图之间的关系
    path("save", views.save),
    path("books", views.books)
]
