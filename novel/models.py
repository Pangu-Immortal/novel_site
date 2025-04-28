from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# 创建小说模型
class Novel(models.Model):
    """
    小说模型：存储小说的基本信息
    title: 小说标题
    cover: 小说封面图片
    introduction: 小说简介
    rating: 小说评分(1-5星)
    created_at: 创建时间
    updated_at: 更新时间
    """
    title = models.CharField(max_length=200, verbose_name='标题')
    cover = models.ImageField(upload_to='covers/', verbose_name='封面', blank=True)  # 小说封面图片
    introduction = models.TextField(verbose_name='简介')  # 小说简介
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, verbose_name='评分')  # 评分，如4.5
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '小说'
        verbose_name_plural = '小说'
        ordering = ['-created_at']  # 按创建时间倒序排列

    def __str__(self):
        """用于在后台显示小说标题"""
        return self.title

# 创建章节模型
class Chapter(models.Model):
    """
    章节模型：存储小说的章节内容
    novel: 关联的小说
    title: 章节标题
    content: 章节内容
    order: 章节顺序
    created_at: 创建时间
    updated_at: 更新时间
    """
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='chapters', verbose_name='所属小说')
    title = models.CharField(max_length=200, verbose_name='章节标题')
    content = models.TextField(verbose_name='内容')
    order = models.IntegerField(default=0, verbose_name='章节顺序')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['order']  # 按章节顺序排列

    def __str__(self):
        """用于在后台显示章节信息"""
        return f"{self.novel.title} - {self.title}"

    def get_previous_chapter(self):
        """获取上一章节"""
        return Chapter.objects.filter(novel=self.novel, order__lt=self.order).order_by('-order').first()

    def get_next_chapter(self):
        """获取下一章节"""
        return Chapter.objects.filter(novel=self.novel, order__gt=self.order).order_by('order').first()


