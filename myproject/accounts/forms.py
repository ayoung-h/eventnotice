from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label= "아이디",
        help_text="",
    )
    password1 = forms.CharField(
        label= "비밀번호",
        widget=forms.PasswordInput,
        help_text="",
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        help_text="",
    )
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]