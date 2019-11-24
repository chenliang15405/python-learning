from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def books(request):
    # 查询数据库中数据并展示
    books = BookInfo.objects.all()
    # 返回到模版
    return render(request, "booktest/book.html", {"books": books})


def save(request):
    # 使用模版文件，传递数据到模版
    # 重定向
    b = BookInfo()
    b.btitle = "123321"
    b.bpub_date = date(1990, 1, 1)
    b.save()
    # 重定向
    # return HttpResponseRedirect("/books")
    # 直接使用重定向即可
    return redirect("/books")


def areas(request):
    # 通过自关联查询谁
    area = AreaInfo.objects.get(atitle="上海市")
    # 查询上级地区，就是查询一的数据
    parent = area.aParent
    # 查询下级地区，查询多的数据
    child = area.areainfo_set.all()
    return render(request, "booktest/book.html", {})
