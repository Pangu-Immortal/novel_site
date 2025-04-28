from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Novel, Chapter
from .forms import UserRegisterForm


def home(request):
    """
    首页视图：显示所有小说列表
    """
    novels = Novel.objects.all()
    return render(request, 'novel/home.html', {'novels': novels})


def novel_detail(request, novel_id):
    """
    小说详情页视图：显示特定小说及其章节列表
    novel_id: 小说的ID
    """
    novel = get_object_or_404(Novel, id=novel_id)
    return render(request, 'novel/novel_detail.html', {'novel': novel})


def chapter_detail(request, novel_id, chapter_id):
    """章节阅读页视图"""
    novel = get_object_or_404(Novel, id=novel_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, novel=novel)

    # 使用模型方法获取上一章和下一章
    prev_chapter = chapter.get_previous_chapter()
    next_chapter = chapter.get_next_chapter()

    context = {
        'novel': novel,
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter
    }
    return render(request, 'novel/chapter_detail.html', context)


def register(request):
    """
    用户注册视图
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 注册后自动登录
            messages.success(request, f'账号创建成功！欢迎 {user.username}！')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def privacy_policy(request):
    """
    隐私政策页面视图
    """
    return render(request, 'pages/privacy.html')


def terms_of_service(request):
    """
    服务条款页面视图
    """
    return render(request, 'pages/terms.html')