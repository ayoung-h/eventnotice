from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.views import LogoutView

class MyLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "성공적으로 로그아웃되었습니다.")
        return super().dispatch(request, *args, **kwargs)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, "가입 신청이 완료되었습니다. 관리자의 승인을 기다려주세요.")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})