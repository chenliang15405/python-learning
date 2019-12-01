from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.

# 自定义模型管理类, 后台管理的展示字段配置
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hcomment", 'name']  # 配置显示的字段， 还可以定义方法(例如：name)

    list_per_page = 10  # 指定每页显示10条数据

    actions_on_bottom = True  # 指定按钮的位置

    list_filters = ['hnmae']  # 页面右侧的过滤栏

    search_fields = ['hname']  # 列表上方的搜索栏


# 后台管理相关文件
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
