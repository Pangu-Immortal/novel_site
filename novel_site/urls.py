"""
URL configuration for novel_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

"""URL配置"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from novel import views as novel_views

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理URL
    # 其他URL配置将在后面添加

    # 网站页面URL
    path('', novel_views.home, name='home'),  # 首页
    path('novel/<int:novel_id>/', novel_views.novel_detail, name='novel_detail'),  # 小说详情页
    path('novel/<int:novel_id>/chapter/<int:chapter_id>/', novel_views.chapter_detail, name='chapter_detail'),  # 章节阅读页

    # 用户认证URL
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # 登录
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # 退出登录
    path('register/', novel_views.register, name='register'),  # 注册

    # 法律页面URL
    path('privacy/', novel_views.privacy_policy, name='privacy'),  # 隐私政策
    path('terms/', novel_views.terms_of_service, name='terms'),  # 服务条款
]

# 开发环境下提供媒体文件访问
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)