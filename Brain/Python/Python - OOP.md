# 클래스, 인스턴스, 객체
클래스는 틀
객체는 틀에서 나온 물건
인스텐스는 객체랑 비슷하지만 어감이 다름
클래스로 인스턴스를 만듬이라는 문장이
클래스로 객체를 만듬이라는 문장보다 자연스러움
인스턴스는 클래스와의 관계를 나타낼때 많이 사용하는 반면
객체는 그냥 그자체로의 의미로 많이 사용한다고 함

# 인스턴스 변수
인스턴스 이름.속성이름(인스턴스 변수)=속성에 넣을 값
class에서 미리 정의한 내용이 아닌 것도 class 밖에서 정의해서 사용할 수 있음

# 인스턴스 메소드

```python
class User:
	def hello(some_user):
		print("hello {}!".format(some_user.name))
```


이렇게 클래스를 정의했을 때,

```python
User.hello(user1)
user1.hello()
```

이 둘은 같은 의미임
왜냐하면 클래스에서 메소드를 호출한 것과 인스턴스에서 메소드를 호출한 것이
차이가 있는데, 인스턴스에서 메소드를 호출하면 해당 인스턴스가
가장 첫번째 인자로 자동으로 전달되기 때문이다.

이때 인스턴스 메소드 첫번째 인자 그러니까 위에 예시에서 some_user는 self로
쓰는 것이 파이썬 세계에서 권장된다.

```python
class User:
def hello(self):
	print("hello {}!".format(self.name))
```



# 매직 메소드(특수 메소드)
특정 상황에서 자동으로 호출되는 메소드
던더 메소드라고도 함

__init__()
인스턴스가 생성될 때 호출됨
인스턴스 생성과 초기화를 한 번에 할 수 있음

__str__()
기본적으로 객체를 출력하면 그 객체의 클래스와 그 객체가 저장된
메모리 주소가 출력된다.
던더str은 객체를 출력했을때 원하는 문자열을 출력하게 해준다.
원하는 문자열을 매개변수로 받아서 리턴해주면 된다.

# 클래스 변수

같은 클래스의 인스턴스가 공유하는 변수

```python
class User:
count=0		#클래스 변수
	
	def __init__(self,name,email):
		self.name=name
		self.email=email
		
		User.count+=1
		
	def hello(some_user):
		print("hello {}!".format(some_user.name))
```

클래스 변수의 값을 접근(변경)할 때
인스턴스.변수이름으로 하든
클래스.변수이름으로 하든
접근은 된다.
그러나 인스턴스 내의 클래스 변수와 같은 이름으로 하는 인스턴스 변수가 있다면
인스턴스.변수이름 으로 접근했을 때 클래스 변수가 아닌 인스턴스 변수로 접근한다.
따라서 클래스 변수를 접근 혹은 변경할 때 꼭 클래스.변수 이름으로 접근 해야한다.

# 데코레이터
함수를 꾸며주는 장치? 기존 함수에 새로운 기능을 추가 시켜주는 무언가 - 좀 더 공부해야됨

```python
def print_hello():
	print("hello")

def add_print_to(original):		#데코레이터 함수
	def wrapper():
		print("start")
		original()
		print("end")
	return wrapper

add_print_to(print_hello)	#아무것도 출력되지 않음

add_print_to(print_hello)()	#start\n hello\n end\n

print_hello=add_print_to(print_hello)
print_hello() 		#start\n hello\n end\n

#@를 이용해서 간단하게 데코레이터 사용하기

def add_print_to(original):		#데코레이터 함수
	def wrapper():
		print("start")
		original()
		print("end")
		
@add_print_to		#데코레이터
def print_hello():
	print("hello")
	return wrapper
	
print_hello()		#start\n hello\n end\n
```


# 클래스 메소드
인스턴스 변수를 다루기 위한 메소드

```python
class User:
	count=0		#클래스 변수

	def __init__(self,name,email):
		self.name=name
		self.email=email

		User.count+=1

	def hello(some_user):
		print("hello {}!".format(some_user.name))

	@classmethod	#데코레이터
	def number_of_users(cls):
		return cls.count	#User.count랑 같음
```


# 인스턴스 메소드와 클래스 메소드의 사용
매개변수가 자동으로 전달되는 이유는 데코레이터를 이용했기 때문
User.say_hello(user1)
user1.say_hello()
User.number_of_users()
user1.number_of_users()

두가지 메소드 구분해서 사용하기
인스턴스 변수가 사용됐다면 인스턴스 메소드를 사용하고
클래스 변수가 사용됐다면 클래스 메소드를 사용하면 됨
둘다 있다면 인스턴스 메소드를 사용함 왜냐하면 인스턴스 메소드는
인스턴스 변수, 클래스 변수 모두 참조 가능하지만 반대는 인스턴스 변수를 못함
만약 둘다 없다면 정적 메소드를 사용하면 된다

기본적으로 함수를 선언하면 인스턴스 메소드, 
데코레이터를 통해 @classmethod를 사용하면 클래스 메소드


# 정적 메소드
인스턴스 변수, 클래스 변수 모두 사용하지 않으면 정적 메소드로 선언하면 된다.
좀 더 직관적으로 말하면, 속성 없이 행동만 하는 객체.

User.staticmethod()	
user1.staticmethod()


# 파이썬은 순수 객체 지향 언어
print(type(2))
print(type("asdf"))
print(type([]))
print(type({}))
print(type(()))
print(type(print_hello))

결과를 출력해 보면 파이썬에 흔히 사용하는 문법들은 모두 class로 정의되어 있음을
알 수 있다.
파이썬은 모든 요소가 객체이기 때문이다.


# 추상화
프로그래머들이 특정 코드를 사용할 때 필수적인 정보를 제외한 세부사항을 가리는 것

ex) 난 아직도 리스트를 사용할 때 어떤 동작이 일어나는지 설명하지 못한다..


# 문서화(docstring)
documentation string	문서화 문자열
아무리 클래스, 메소드, 변수 등의 이름을 잘 지어도 이해하는데 한계가 있다.
직관적인 이해를 돕기 위해 코드 내의 코드의 설명을 적어 놓는 것
클래스 메소드 아래에다가 큰따음표 3개 사이에 원하는 주석을 달면 됨

```python

class User:
	"""유저 클래스"""
	def hello(some_user):
		"""인사말을 출력하는 메소드"""
		print("hello {}!".format(some_user.name))
		
#이렇게 docstring을 해놓으면 장점이 하나 더 있다.

help(User)

#이런 식으로 help의 인자로 넘기면 요약된 형태로 class를 한 눈에 확인 할 수 있다.

#아래는 google docstring 이다.

def find_suggestion_videos(self, number_of_suggestions=5)

"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
	(기본값은 5)

Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""
```


# type hinting
파이썬은 동적타입언어임 즉,변수의 타입이 정해져있지 않음
파이썬은 python 3.5부터 이러한 문제를 해결하기 위해 type hinting을 만듬
각종 변수, 파라미터, 리턴값 등의 타입을 정해줄 수 있음

```python
class User:
	count: int=0

	def __init__(self,name: str,email: str)->None:
		self.name=name
		self.email=email

```


# 캡슐화
객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것
언더바 2개로 숨기고 싶은 변수나 메소드를 설정 할 수 있음
변수를 직접 사용하는 부분을 최소화해야 유지보수하기 쉬워짐

```python
class User:
	count=0

	def __init__(self,name,email):
		self.name=name
		self.email=email
		self.__pw=pw
		
	def auth(self, input):
		return self.__pw==input
		
	def __show_pw(self):
		return self.__pw
	
assert(User.__pw)		#attribute 에러
assert(User.__show_pw())	#attribute 에러
```
		

이런 식으로 아래바 2번로 변수를 숨기면 클래스 외부에서 액세스가 불가능 해진다.
이 문제를 해결하려면 변수를 액세스하는 메소드를 만들면 된다.

```python
class User:
	count=0

	def __init__(self,name,email):
		self.name=name
		self.email=email
		self.__pw=pw
		
	def auth(self, input):
		return self.__pw==input
		
	def get_pw(self):
		return self.__pw
		
	def set_pw(self, new_pw):
		self.__pw=new_pw
```
		
특정 변수를 받아오는 메소드를 getter메소드
설정하는 메소드를 setter메소드

### 파이썬에서의 캡슐화 문화
파이썬에서는 언더바 하나로 클래스 내부에 있는 변수의 접근을 막는 경우가
많음.
언더바 2개(네임 맹글러)를 사용하면 실수로 인한 접근을 막을 수 있다는 장점이
있고, 네임 맹글러는 접근을 거의 막는다. 
완전히 막지는 못하는데, _클래스명__변수 이런 식으로 이름이 바뀌는 것 
뿐이지 실제로 막지는 못하기 때문이다.
그래서 언더바 하나로 막는데, 언더바 하나도 강제적으로 막지 못하지만
경고를 띄워서 다른 개발자가 경고를 지키지 않고 만들었을 때 생기는 문제를
책임지게 만들 수 있다.

### 데코레이터를 사용한 캡슐화
캡슐화를 get_pw 이런식으로 하는 것도 괜찮지만
데코레이터를 사용하면 코드 수정을 최대한 줄일 수 있다.

```python
class User:
	count=0

	def __init__(self,name,email,pw):
		self.name=name
		self.email=email
		self._pw=pw

	def auth(self, input):
		return self._pw==input

	@property
	def pw(self):
		return self._pw

	@pw.setter
	def pw(self,value):
		self._pw=value

Tom=User('tom','hammer@asdf.com','secret')

print(Tom.pw)

Tom.pw='I feel lucky'

print(Tom.pw)
```

@property 데코레이터를 사용하면 getter 메소드를 사용하는 것과
동일하고, @인스턴스변수.setter 데코레이터를 사용하면 setter메소드를 
사용하는 것과 동일하다.
주의해야할 점은 위에서 인스턴스 변수라고 표현 했지만 사실 인스턴스 변수가
아니라는 점이다. 왜냐하면 실제 인스턴스 변수는 _pw이고 pw()라는 메소드를
호출하는 구조기 때문이다.
즉, @pw.setter가 붙으면 인스턴스 변수 pw에 어떤 값을 설정한다는
원래의 뜻이 아니라 setter 메소드 pw를 실행한다는 의미로 바뀌는 것

# 상속
A는 B이다의 관계가 성립한다면 A는 자식클래스이고, B는 부모클래스이다.
자식클래스에서 부모클래스와의 상속관계를 파이썬 코드로 나타내고 싶다면
아래와 같이 나타내면 된다.

class 부모클래스:
	pass

class 자식클래스(부모클래스):
	pass
	
### mro(method resolution order) 메소드
자식클래스를 help메소드로 호출하면 이 클래스가 어떤 메소드와 변수를
사용할 수 있는지뿐만 아니라	어떤 부모 클래스가 있는지 나타내는
"Method resolution order:" 라는 부분이 있다.
이 때 object 클래스를 상속하지 않았음에도 상속되어 있는 모습을 확인할
수 있는데 파이썬은 모든 것이 class로 이루어져 있기 때문에 가능하다.

mro는 메소드 검색 순서를 뜻한다.

```python
>>> list.mro()
[<class 'list'>, <class 'object'>]
```

만약 자식클래스에서 부모클래스를 오버라이딩 했다면
자식클래스에서 접근할 수 있는 메소드는 3가지가 있을 것이다.
즉, 자식클래스, 부모클래스, object클래스 각각 내부에 접근할 수 있는 메소드
중에서 아무거나 고르는게 아니라 mro() 메소드에 나와있는 순서대로 찾는다는
뜻이다. 그리고 그 순서는 자식클래스에서 부모클래스 순서로 정렬되어 있다. 
예를들어 list.mro()를 호출하면 list클래스에는 mro라는
메소드가 없기 때문에 object클래스에 가서 찾을 것이다.

### isinstance 메소드
isinstance 함수는 어떤 인스턴스가 주어진 클래스의 인스턴스인지를 알려준다.
isinstance(`[검사할 인스턴스의 이름]`,`[기준 클래스의 이름]`)->불린

### issubclass 메소드
issubclass 함수는 한 클래스가 다른 클래스의 자식클래스인지를 알려준다.
issubclass(`[검사할 클래스의 이름]`,`[기준이 되는 부모 클래스의 이름]`)->불린

### 오버라이딩
부모클래스를 자식클래스가 상속을 받기만 하면 상속받은 모든 자식클래스는
모두 동일한 클래스가 될 것 이다. 따라서 자식클래스들은 각자의 다른 기능을 
하기 위해 오버라이딩을 해야한다.

```python
class Employee:
	"""직원 클래스"""
	raise_percentage=1.03

	def __init__(self,name,wage):
		self.name=name
		self.wage=wage

	def raise_pay(self):
		self.wage+=self.raise_percentage

class Cashier(Employee):
	def __init__(self,name,wage,number_sold):
		super().__init__(name,wage)
		self.number_sold=number_sold
		
class DeliveryMan(Employee):
	pass
```
		
오버라이딩을 할 때, 수정하거나 추가해야하는 부분을 고치면 되는데
부모클래스에 있는 메소드를 같은 이름의 메소드로 자식에 생성하면 된다.
한편 수정해야할 메소드에서 같은 부분이 있을 수도 있다.
위에서처럼 __init__()를 수정해야 한다면,

	self.name=name
	self.wage=wage
	self.number_sold=number_sold

처럼 수정할 수 있다. 그러나 이보단 처음 예시처럼 super()를
사용하는 것이 바람직하고, 이렇게 super()를 사용했다면 매개변수 self를 
사용하지 않아도 된다.

그 외에 오버라이딩 할 필요가 없는 각각의 자식클래스만의 기능들은 자식클래스에
그대로 적어주면 된다.
		
다중상속
하나의 객체가 여러가지 특징을 가질 수도 있다. 이럴 때 사용하는 것이
다중상속이다. 다중상속은 괄호 안에 부모클래스를 ,로 구분해서 구현한다.

	class Cashier(Employee,dad):

super()를 사용하면 여러 부모클래스 중에 어떤 부모클래스인지 알 수가 
없기 때문에 어떤 클래스를 사용할 것인지 명시를 해줘야한다. 
이를 피하려면	부모클래스끼리 같은 이름의 메소드를 갖지 않도록 하고
만약 불가피하게 같은 이름의 메소드를 가지게 된다면 자식클래스에서
오버라이딩을 해서 확실하게 호출 위치를 정해줄 수도 있다.
만약 발생했다면 object.mro()를 통해 호출 순서를 확인할 수 있다.

이러한 특성 때문에 다중 상속은 되도록 하지 않거나 하더라도 주의해서
해야한다만 이러한 주의는 일반클래스에서만 이고,
추상클래스에서는 그렇지 않다. 자세한 내용은 다형성-추상클래스


# 클래스 다형성
한 변수가 다양한 인스턴스를 가질 수 있을 때 다형성이 있다고 표현한다.

### 추상클래스
한 변수가 다양한 인스턴스를 가질 수 있게 만들게되면
관련없는 인스턴스가 변수나 클래스의 메소드를 사용하게되면
관련없는 인스턴스의 클래스에는 해당 변수, 메소드가 없기 때문에
오류가 나올 것이다. 이러한 문제는 상속을 통해 해결할 수 있는데
일반 상속 또한 메소드 오버라이딩을 강제하지 않기 때문에 
추상 클래스를 통해 오버라이딩을 시켜야 한다.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass
		
	@abstractmethod
	def perimeter(self):
		pass
```

abc 모듈에 ABC클래스와 abstractmethod 데코레이터 함수를 가져와
추상 클래스로 만들려고 하는 클래스에 ABC를 상속시키게 만들고
강제로 오버라이딩 하게 만들고 싶은 함수에
abstractmethod 데코레이터를 사용하면 된다.
이렇게 추상메소드를 구현하면 area(), perimeter()를 오버라이딩
하지 않은 클래스는 오류를 발생시킬 것이다.
또한, isinstanceof Shape 이런 구문을 통해 해당 추상클래스를
상속하는지 여부를 체크하여 오버라이딩 되어 있다는 보증이된 
인스턴스만 true로 리턴하게 만들 수도 있다.

Shape 클래스로 추상화된 수준까지만 고려하기만 하기 때문에
이렇게 다형성을 구현함과 동시에 추상화도 한것이라고 이야기 할 수 있다.

	def add_shape(self, shape: Shape):

다음과 같이 type hinting 기능 또한 사용한다면 더 좋은 코드가 된다.

추상클래스에는 내용을 추가할 수도 있는데, 공통되는 내용을
작성한 후 super()을 통해 접근할 수 있다.

	def area(self):
		"""직사각형의 넓이를 리턴한다"""
		super().area() # 
		return self.width * self.height

특정 변수를 가지도록 유도할 수도 있는데, @property, @x.setter와
같은 데코레이터에 @abstract를 합쳐서 사용하면 특정 변수의 사용을
유도할 수 있다.

```python
class EquilateralTriangle(Shape):
	 """정삼각형 클래스"""
	def __init__(self, x, y, side):
		self._x = x
		self._y = y
		self.side = side

	def area(self):
		"""정삼각형의 넓이를 리턴한다"""
		return sqrt(3) * self.side * self.side / 4

	def perimeter(self):
		"""정삼각형의 둘레를 리턴한다"""
		return 3 * self.side

	@property
	@abstractmethod
	def x(self):
		"""_x getter 메소드"""
		return self._x

	@x.setter
	@abstractmethod
	def x(self, value):
		"""_x setter 메소드"""
		self._x = value

	@property
	@abstractmethod
	def y(self):
		"""_y getter 메소드"""
		return self._y

	@y.setter
	@abstractmethod
	def y(self, value):
		"""_y setter 메소드"""
		self._y = value

equilateral_triangle = EquilateralTriangle(5, 6, 4) # 에러가 나지 않는다
equilateral_triangle.x = 10
print(equilateral_triangle.x) # 출력: 10

equilateral_triangle.y = 5
print(equilateral_triangle.y) # 출력: 5
```
	
추상클래스에서의 다중상속
위에서도 언급했듯이 추상클래스에서 다중상속은 자주 사용됨

```python
class Message(ABC):
	@abstractmethod
	def print_message(self) -> None:
		pass

	@abstractmethod
	def send(self, destination: str) -> None:  # ----- 중복되는 추상 메소드
		pass

class Sendable(ABC):
	@abstractmethod
	def send(self, destination: str) -> None: # ----- 중복되는 추상 메소드
		pass
```

이렇게 두 자식클래스에서 모두 send()를 갖도록 하더라도
어차피 둘 다 자식클래스에서 send()를 반드시 갖도록 유도하였으므로
두가지 추상클래스에서 사용된 코드가 아닌 자식클래스에서의 send()가
사용되기 때문에 문제가 없다. 결국엔 추상클래스는 오버라이딩을 
강제하기 때문에 일반클래스의 다중상속보다 좋은 것이다. 그러나
추상클래스를 사용하더라도 일반메소드를 사용할 수도 있고, 같은 이름의
일반 메소드가 부모클래스가 사용되는 경우가 있을 수도 있긴하다. 
이러면 사실상 일반 클래스간에 같은 이름을 갖는 메소드와 같이 문제가
생길 것이다.


# 함수/메소드 다형성
### 옵셔널 파라미터
기본값을 미리 지정해준 파라미터 
옵셔널 파라미터는 항상 가장 뒤에

	def new_print(value1,value2=none):

### 파라미터 이름 명시
함수를 호출할 때 파라미터 이름 표시하는 것을 말함

	new_print(value1=1,value2="qwerty")

### 개수가 확정되지 않은 파라미터
마지막 파라미터 이름 앞에 *를 사용하면 됨

	def print_msg(name,*msg):
	
msg라는 이름의 튜플에 담김


# LBYL,EAFP 코딩 스타일
LBYL(LOOK BEFORE YOU LEAP)	돌다리도 두드려보고 건너자!
어떤 작업을 수행하기 전에 그 작업을 수행해도 괜찮을지 확인
isinstanceof 와 같은 사전 필터링을 사용함

EAFP(EASIER TO ASK FOR FORGIVENESS THAN PERMISSION) 허락보다 용서가 쉽다
일단 실행하고 문제가 생기면 처리
try except 와 같은 에러처리 구문을 사용함


# `__builtin__` 외 사용 불가일 경우

```python
`().__class__.__bases__[0].__subclasses__()[40]`
```

이런 식으로 우회할 수 있음!

# TIPS
class 이름은 항상 대문자로 시작
객체는 속성(변수)과 행동(메소드)의 조합

# ABC