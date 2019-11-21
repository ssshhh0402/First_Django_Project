from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auth_login(request, user)          --> 회원가입후 바로 로그인 시켜주는 코드
            return redirect('accounts:signup')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html', context)
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #로그인
            auth_login(request, form.get_user())
            return redirect (request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

    #user.is_authenticated = 로그인 되어 있는지/아닌지 return 해주는 변수
    #is_staff? = staff 인지 일반 회원인지 superuser인지 판단하는  변수
    #request.user.is_anonymous = 로그인이 안되어 있는 상태인지 확인
    #last_login: 마지막으로 로그인한 날짜 반환


def u_inf(request):
    # u = User.objects.get(username = u_id)
    # u.set_password(request.POST)
    # u.save()
    form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)