from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """
    用户注册表单：扩展Django默认的UserCreationForm，
    添加email字段，并自定义错误消息
    """
    email = forms.EmailField(required=False, help_text='可选。请输入有效的电子邮件地址。')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义错误消息
        for field in self.fields:
            self.fields[field].error_messages = {
                'required': f'请填写{self.fields[field].label}',
                'invalid': '请输入有效的值',
                'max_length': f'{self.fields[field].label}太长',
                'min_length': f'{self.fields[field].label}太短',
            }