[toc]

# django에 css 입혀보는 실습

- 백엔드에 대한 학습을 여러번 진행해보았는데, 프론트쪽도 조금 배워보고 싶어서 하나씩 적용해보는 중이다.
- css를 프론트에 입히는 것은 상당히 어려웠다.
- 하지만 한번 실습을 해보니까 재밌었고, 내 것으로 소화할 수 있을 것 같았다.

## 1) init script

```bash
pip3 install django==2.1.5
python manage.py startproject config .
python manage.py startapp testCss
```

## 2) Settings 설정

```python
INSTALLED_APPS = [
    ...
    'cssTest',	# 앱 추가
]
```

```python
LANGUAGE_CODE = 'ko'	# 한국어 설정

TIME_ZONE = 'Asia/Seoul'	# 시간 한국 설정
```

```python
# 맨 밑에 추가

# (필수) 정적 이미지, css, js 를 설정해야하므로 추가해야 함.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# (선택) 이미지나 동영상을 보관할 미디어 파일 경로를 설정하려면 추가할 것.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

- static : img 저장소
- templates : base.html 관리소

![image](https://user-images.githubusercontent.com/26649731/76835571-b1fe1280-6872-11ea-9dd5-aff9030e2ffb.png)

- 파일 구조는 이렇게 형성되면 기본을 잡는 것이다.

## 3) base.html 작성

- 원래는 뷰와 url을 먼저 짜야하지만 이번에는 프론트 부분에 대해 알아볼 것이기 때문에 프론트 먼저 짠다.
- `<project-name>/ templates/base.html`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.css">
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <title>Document</title>
</head>
<body>

    {% block content %}
    {% endblock %}

</body>
</html>
```

- `<app-name>/templates/<app-name>/index.html`

```html
{% extends 'base.html' %}
{% block content %}
{% load static %}
{% load staticfiles %}
<link rel="stylesheet" href="{% static 'css/testCss.css' %}">

    <header class="header">
        <div class="header-inner">
            <div class="box1">
                <div class="header-site">
                    <h1><a href="#"><img src="{% static 'img/06/logo-large.png' %}" alt="Business"></a></h1>
                </div>
            </div>
            <div class="box2">
                <button type="button" id="header-menubtn">
                    <i class="fa fa-bars"></i><span>MENU</span>
                </button>
                <nav class="header-nav" id="menu">
                    <ul>
                        <li><a href="#">메인</a></li>
                        <li><a href="#">연혁</a></li>
                        <li><a href="#">사업 소개</a></li>
                        <li><a href="#">채용 정보</a></li>
                        <li><a href="#">문의</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>
...
{% endblock %}
```

- 필자가 사전에 꾸며놓은 이미지 파일을 넣기 위해서 `{% load staticfiles %}`을 불러와야 하고,
- 정적 css 파일을 로드하기 위해 `{% load static %}`를 불러와야 한다.
- html 을 확장시키기 위해 `{% extends 'base.html' %}, {% block content %}`이 필요하다.

## 4) View 코딩

- 간단한 css 실습이므로 따로 모델은 작성하지 않았음.
- 따라서 바로 뷰를 코딩한다.

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.init),
]
```

```python
from django.shortcuts import render

# Create your views here.
def init(request):
    return render(request,'cssTest/index.html')
```

![image](https://user-images.githubusercontent.com/26649731/76836189-c098f980-6873-11ea-8325-1a425cd9e148.png)

- css가 잘 적용되었다.