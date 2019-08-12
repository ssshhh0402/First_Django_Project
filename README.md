#  Django

## 0.시작하기 전에

Django 성격: 1) Opisionated(다소 독선적) -  Django에서 정의한 설정? 등을 우리가 따라서 사용해야 한다.

Framework vs Library:

​	Library(기능 구현)을 사용하여 Framework 구현!		

static vs dynamic?

​	static: 구현자(나)가 사전에 정의한 대로만 보여짐

 	dynamic: 실시간으로 변화?

기본 웹 페이지: M(odel)V(iew)C(ontrol)

Django : M(odel)T(emplate)V(iew)



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

* 프로젝트이름으로 구성된 폴더와 `manage.py`가 생성된다.
  * `__init__.py `: 해당 폴더가 패키지로 인식될 수 있게끔 작성되는 파일 
  * `settings.py`: django 설정과 관련된 파일
  * `urls.py`: **url 관리**
  * wsgi.py`: 배포시 사용(Web Server Gateway Interfate : 파이썬에서 사용되는 웹 서버)
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