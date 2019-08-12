from django.shortcuts import render

# Create your views here.
# 요청을 처리할 함수 정리
def index(request):
    # 2. >>로직 작성<<
    # 3. 해당하는 템플릿 리턴
    return render(request, 'index.html')

    
def hello(request,name):
    context = {'names': name}
    return render(request, 'hello.html', context)



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
    return render(request, 'lotto.html', context) 

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
    return render(request, 'dinner.html', context)


# render 함수 필수 인자: request, template 파일
# 변수를 넘겨주고 싶으면 3 번째 인자로 dicttionary를 넘겨준다.
# Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)!