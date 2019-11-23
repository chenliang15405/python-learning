from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.

# 自定义模型管理类, 后台管理的展示字段配置
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hcomment"]


# 后台管理相关文件
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
