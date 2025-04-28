from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Novel, Chapter

# 章节内联显示（在小说详情页面内直接管理章节）
class ChapterInline(admin.TabularInline):
    """章节内联管理器：在小说详情页面直接管理章节"""
    model = Chapter
    extra = 1  # 默认显示一个空的章节表单

# 小说管理器
@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    """小说后台管理配置"""
    list_display = ('title', 'rating', 'created_at', 'updated_at')  # 列表显示的字段
    list_filter = ('rating',)  # 过滤选项
    search_fields = ('title', 'introduction')  # 搜索字段
    inlines = [ChapterInline]  # 内联显示章节

# 章节管理器
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    """章节后台管理配置"""
    list_display = ('title', 'novel', 'order', 'created_at')
    list_filter = ('novel',)  # 可按小说过滤
    search_fields = ('title', 'content')  # 可搜索标题和内容