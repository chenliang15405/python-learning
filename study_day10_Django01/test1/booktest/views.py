from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo

# Create your views here.

# 定义渲染模版函数
def my_render(request, template_path, context_dict={}):
    # 1. 加载模版文件
    temp = loader.get_template(template_path)
    # 2. 定义模版上下文
    context = RequestContext(request, context_dict)
    # 3. 模版渲染，生成html内容
    res_html = temp.render(context)
    return HttpResponse(res_html)


# 定义视图函数， 参数为HttpRequest
# 需要返回一个HttpResponse对象
def index(request):
    return HttpResponse("Hello World")


def index2(request):
    # 使用模版文件，传递数据到模版
    #  return my_render(request, "booktest/index.html")
    # 可以直接使用django中定义好的render渲染模版
    # 并通过第三个参数传递数据
    return render(request, "booktest/index.html", {"content": "hello word", "list": list(range(1, 10))})


def books(request):
    # 查询数据库中数据并展示
    books = BookInfo.objects.all()
    # 返回到模版
    return render(request, "booktest/book.html", {"books": books})


def book_detail(request, bid):
    # 查询数据库中数据并展示
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()

    # 返回到模版
    return render(request, "booktest/book_detail.html", {"book": book, "heros": heros})
