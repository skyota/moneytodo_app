from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

# アカウントの登録
def accounts_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user')
    else:
        form = SignupForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/signup.html', params)

# ログイン
def accounts_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('user')
    else:
        form = LoginForm()
    params = {
        'form': form,
    }
    return render(request, 'accounts_app/login.html', params)

# ログアウト
@login_required
def accounts_logout(request):
    logout(request)
    return render(request, 'accounts_app/logout.html')

# ユーザー情報
@login_required
def accounts_user(request):
    user = request.user
    params = {
        'user': user,
    }
    return render(request, 'accounts_app/user_info.html', params)