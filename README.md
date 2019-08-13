#  Django

## 0.시작하기 전에

### 0.Django 설명

Django 성격: 1) Opisionated(다소 독선적) -  Django에서 정의한 설정? 등을 우리가 따라서 사용해야 한다.

Framework vs Library:

​	Library(기능 구현)을 사용하여 Framework 구현!		

static vs dynamic?

​	static: 구현자(나)가 사전에 정의한 대로만 보여짐

 	dynamic: 실시간으로 변화?

기본 웹 페이지: M(odel)V(iew)C(ontrol)

Django : M(odel)T(emplate)V(iew)

### 1. 가상환경 실행 + .gitignore!

* 가상환경을 사용하는 이유는 프로젝트마다 활용되는 라이브러리가 다르고, 동일한 라이브러리더라도 버전이 다를 수 있다.
* 따라서 프로젝트 하면서 라이브러리 삭제 혹은 변경을 하는 것이 아니라 각 프로젝트마다 독립된 가상환경을 부여하여 의존성을 없앤다.
* 그러니까 Django 할때마다 activate 좀 하기
* 추후에 D(ata)S(cience)/M(achine)L(eaning)/D(ata)L(earning) -> anaconda 활용하기도 한다! 

* 가상환경은 Python에서 기본으로 제공하고 있는 [`venv`](https://docs.python.org/ko/3/library/venv.html)를 활용한다.(Python 3.5++) 

  * 1. 가상환경 생성

    ```bash
    $python -m venv __venv__
    ```

    * `__venv__`여기에 가상환경 이름을 작성하는데, 보통 `venv`라고 설정한다.
    * `__venv__`폴더가 생성되는데, 구조는 다음과 같다.
      * `Lib` : 가상환경에 설치된 라이브러리 모음 만약 
      * `Scripts` : 가상환경 실행과 관련된 파일

  * 2. 가상환경 실행

    ```bash
    $ls
    venv/ ...
    $ source venv/Scripts/activate
    (venv)
    $ python -V
    Python 3.7.4
    ```

    * 반드시 해당 명령어는 `venv`폴더가 있는 곳에서 실행시킨다.
    * **`bash shell`에서는 `activate`파일을 실행하여야 한다.**
      * `cmd`: `activate.bat`
      * `power shell` : `activate.ps1` 

  * 3. 가상환경 종료

    ```bash
    $ deactivate
    ```

  * 4. `.gitignore` 등록

    ```bash
    venv/
    ```

    * 추가적으로 visual studio code를 활용하는 경우에는 `vscode/`
    * python 환경에서는 `__pycache__/`
    * pycharm 환경에서는 `.idea/`
    * 위의 폴더들은 `.gitignore/`에 등록하는 습관 가지기 잘 모르겠으면 [gitignore.io](https://www.gitignore.io)에서 검색해서 등록하기 

## 1. 시작하기

```bash
$ pip instsall django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * Python 3.7.4
  * Django 2.2.4

### 1.Django프로젝트 시작

```
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름 __ 
```

```bash
$ django-admin startproject ___프로젝트이름_____ .
```

* 주의!!! 맨 끝에 `.` 찍어야 하는거 기억!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
* 프로젝트이름으로 구성된 폴더와 `manage.py`가 생성된다.
  * `__init__.py `: 해당 폴더가 패키지로 인식될 수 있게끔 작성되는 파일 
  * `settings.py`: django 설정과 관련된 파일
  * `urls.py`: **url 관리**
  * `wsgi.py`: 배포시 사용(Web Server Gateway Interfate : 파이썬에서 사용되는 웹 서버)
  * `manage.py`: **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티**

### 2.서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000` 으로 들어가서 로켓확인!



### 페이지 출력하는 법?

1) urls.py에 url 정의

2) views.py 함수 정의

3) templates/__ html 에서 View 생성





### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

* `App 이름` 인 폴더 생성 , 구성하고 있는 파일은 다음과 같다.

  * `admin.py`: 관리자 페이지 설정(나중에)

  * `apps.py`: app의 정보 설정.(직접 수정하는 경우 별로 없음)

  * `models.py` : **MTV-Model을 정의 하는 곳**

  * `tests.py` : 테스트 코드를 작성하는 곳

  * `views.py` : **MTV-View를 정의 하는 곳**

    *  사용자에게 요청이 왔을 때, 처리되는 함수

    ```html
    def index(request):
    	return render(Request, index.html) 
    ```



**app을 만들고 나서 반드시 `settings.py`에서 `INSTALLED _APPS`에 APP을 등록한다. **

```html
# first_django/settings.py
# ..
INSTALLED_APPS = [
'PAGES',
'DJANGO.CONTRIB.ADMIN',
......
]
*..
```

## 2. 작성 흐름

### 1. URL 정의

```PYTHON
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index),
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 가장 먼저 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
* `path(경로, views에 정의된 함수)`

### 2. View 정의

```Python
# pages/views.py
def index(request):
    return render(request, 'index.html')
```

* `views.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.



### 3. Template 정의

* 기본적으로 app을 생성하면 templates 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/temp;lates/index.html ->
<h1>
장고 ㅎㅇ
</h1>
```



### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

* localhost:8000 확인!







## 3. Django 기본 용법

### 1. views안에서 변수 저장하여 화면 render 하기

```python
# views.py
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
```

```html
# dinner.html 
<h1>오늘 저녁은 {{pick}} 먹어</h1>
  <h2> 1. 반복문</h2>
  {% for menu in menus %}
  <li>{{menu}}</li>
  {% endfor %}
  {% for menu in menus %}
  <p>{{forloop.counter}}:{{menu}}</p>
  {% endfor %}
  {% for user in users %}
  <p>{{user}}</p>
  {% empty %}
  <p>현재 가입한 유저가 없습니다!</p>
  {% endfor %}


<hr>
  <!-- 2. 조건문-->
  {% for menu in menus %}
    {%if menu == '치킨'%}
      <p>치킨은 프라닭</p>
    {% else %}
      <p> 치킨 미만 잡</p>
    {% endif %}
  {% endfor %}

  <!-- lorem-->
  <hr>
  <h2>3. Lorem ipsum</h2>
  <p>{% lorem %}</p>
  <p>{% lorem 3 w %}</p>
  <p>{% lorem 3 p %}</p>
  <p>{% lorem 2 w random %}</p>
    <!-- Lorem 갯수 w/p
    w : word
    p : paragraph-->
    <hr>
  <h2>글자 관련 필터</h2>
  <p>{{ sentence|truncatewords:3 }}</p>
  <p>{{ sentence|truncatechars:10}}</p>
  <p>{{ sentence|length }}</p>
  <p>{{ sentence|lower}}</p>
  <p>{{ sentence|title}}</p>
  <p>{{ menus|random}}</p>
<hr>
  <h2>5. 날짜표현</h2>
  <p>{{datetime_now }}</p>
  <P>{% now 'DATE_FORMAT' %}</P>
  <p>{% now 'DATETIME_FORMAT' %}</p>
  <p>{% now 'SHORT_DATETIME_FORMAT' %}</p>
  <P>{% now 'Y년  m월!' %}</P>
  <p>{{ datetime_now|date:'SHORT_DATE_FORMAT'}}</p>

  <hr>
  <h2>자세한건 여기로</h2>
  <p>{{google_link|urlize}}</p>
  <h2>여기도</h2>
  <p>{{google_link2|urlize}}</p>
```



### 2.url을 통하여 변수 보내주기

1. url을 통하여 어떤 형태의 변수를 받을 것인지 선언

```python
 path('hello/<str:name>/', views.hello)
```

2. 함수안에서 인수로 호출(단, 이때 이름(name)과 1번에서 정의한 이름(name)은 동일해야한다.)

```python
def hello(request,name):
    context = {'names': name}
    return render(request, 'hello.html', context)
```

3. html파일에서 동일하게 호출하여 사용

```html
<body>
  <h1> 안녕 {{names}}/h1>
</body>
```





### **Django Project 생성 흐름**

1. 폴더 생성  

```bash
$mkdir _
```

2. 가상환경 생성

```bash
$python -m venv venv
```

3. 가상환경 실행

```bash
$source venv/Scripts/activate
```

4. 원하는 django 버전 설치

```bash
$pip install django
```

5. 프로젝트 생성

```html
$django-admin startproject ___ .
```

6. 서버 확인

```bash
$python manage.py runserver
```

7. 페이지 추가?

```bash
$python manage.py startapp ___
```

8. url 생성
9. views.py 설정
10. templates 설정
11. 서버 실행