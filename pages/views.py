from django.shortcuts import render
USERS = {}
# Create your views here.
# 요청을 처리할 함수 정리
def index(request):
    # 2. >>로직 작성<<
    # 3. 해당하는 템플릿 리턴
    return render(request, 'pages/index.html')

    
def hello(request,name):
    context = {'names': name}
    return render(request, 'pages/hello.html', context)



def lotto(request):
    # 로직
    import random
    numbers = random.sample(range(1, 46), 6)
    print(request)
    print(type(request))
    print(request.META)
    # 변수를 넘길 때에는 딕셔너리에 담아서 전달
    context = {'numbers': numbers, 'type':type(request),'request':request}
    # render 할때 3번째 인자로 넘겨준다.
    return render(request, 'pages/lotto.html', context) 

def dinner(request):
    import random, datetime
    menus = ['롯데리아', '편도', '맘스터치', '응급실떡볶이', '파파존스', '후참집','피자','치킨']
    pick = random.choice(menus)
    context={'pick': pick, 'menus': menus,
    'users': [],
    'sentence': 'Life is short, You need Python + django!',
    'datetime_now': datetime.datetime.now(),
    'google_link': 'https://docs.djangoproject.com/en/2.2/ref/templates/language/',
    'google_link2': 'https://docs.djangoproject.com/en/2.2/ref/templates/builtins/'}
    return render(request, 'pages/dinner.html', context)


# render 함수 필수 인자: request, template 파일
# 변수를 넘겨주고 싶으면 3 번째 인자로 dicttionary를 넘겨준다.
# Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)!


def cube(request, num):
    context={
        'number': num**3,
        'numbers':[1,2,3],
        'phont':{'a':1, 'b':2, 'c':3}
    }
    return render(request, 'pages/cube.html', context)

def about(request, name, age):                             #여기서 불러오는 값하고 urls에서 지정한 값하고 동일해야 함!
    context={
        'name': name,                 
        'age': age
    }
    return render(request, 'pages/about.html', context)



def gwangbok(request):
    import datetime
    now_time = datetime.datetime.now()
    n_time = now_time.strftime('%m%d')
    stg = ''
    if n_time == '0815':
        stg = '예'
    else:
        str = '아니요'
    
    context= {
        'date': n_time,
        'str': str,
        'time': now_time.time()
    }
    return render(request, 'pages/gwangbok.html', context)



def ping(request):
    return render(request, 'pages/ping.html')


def pong(request):
    #사용자가 넘겨주는 값 받아오기
    print(request.GET)                        #QueryDict
    data = request.GET.get('datas') 
    context = {
        'data': data
    }
    return render(request, 'pages/pong.html', context)


def log(request):
    return render(request, 'pages/log_in.html')

def sign(request):
    return render(request, 'pages/sign_up.html')

def okay(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    pwd2 = request.POST.get('pwd2')
    global USERS
    if pwd == pwd2 and pwd and pwd2 != 0:
        result = True
        USERS[id] = pwd
    else:
        result = False
    context = {
        'result' : result,
    }
    return render(request, 'pages/okay.html', context)

def inner(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    if id in USERS.keys():
        if USERS[id] == pwd:
            context = {
                'id' : id,
                'pwd' : pwd,
                'str' : '로그인 완료'
            }
        else:
            context={
                'str' : '비밀번호 불일치'
            }
        
    else:
        context= {
            'str': '아이디 잘못 입력'
        }
    
    return render(request, 'pages/inner.html', context)


def game(request):
    return render(request, 'pages/game.html')

def rsp(request):
    import random
    choice = request.GET.get('choice')
    c_choice = random.randint(0,2)
    if choice == 'rock':
        y_choice = 0
    elif choice == 'scissor':
        y_choice = 1
    elif choice == 'paper':
        y_choice = 2
    
    if y_choice == 0:
        if c_choice == 1:
            result = '이김'
        elif c_choice == 2:
            result='짐'
        else:
            result = '비김'
    elif y_choice == 1:
        if c_choice == 2:
            result ='이김'
        elif c_choice == 0:
            result='짐'
        else:
            result = '비김'
    elif y_choice == 2:
        if c_choice == 0:
            result ='이김'
        elif c_choice == 1:
            result='짐'
        else:
            result = '비김'
    context={
        'result': result
    }
    return render(request,'pages/rufrhk.html', context)