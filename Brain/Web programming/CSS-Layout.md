# Position
position 속성으로 위치의 기준을 잡고
top bottom right left 이런 속성으로 구체적인 위치를 잡는다.

### static
position 속성의 기본 값
원래 있어야할 위치에 배치
일반적인 글의 흐름을 따른다.


### relative
상대적인 이라는 뜻
원래 있어야 될 곳을 기준으로 함

	position: relative;
	top: 30px;

margin이랑 다른 점은 position은 딱 그 요소만 이동하고
margin은 모든 요소가 이동한다.


### absolute
포지셔닝이 된 가장 가까운 조상 요소를 기준으로 함
즉 static이면 안됨

	position: absolute;
	bottom: 40px;

포지셔닝이 되야지만 선택됨 안되있으면 그 조상을 찾음

absolute 는 자리를 차지하지 않은 것 처럼 됨
즉 두 요소가 나란히 있고 첫번째 요소가 나오고 
두번째 요소가 나오는게 일반적인 흐름이라면
첫번째 요소에 absolute를 주고 두번째에 안줬다면
두번째는 첫번째 자리에 있을 것이다.

absolute 포지션은 width 옵션을 주지 않으면
block 요소더라도 content의 크기 만큼 크기를 가짐 

조상 요소의 크기를 덮고 싶다면

	top: 0;
	bottom: 0;
	left: 0;
	right: 0;

이렇게 하면 된다. 더 간결한 방법은 다음과 같다.

	inset: 0;

또, 조상 요소로 부터 일정한 간격을 주려면 다음과 같다.

	inset: 10px;


### fixed
브라우저 화면 기준으로 고정된 위치를 가짐
스크롤을 하더라도 원래 위치에 있고
absolute처럼 자리를 차지하지 않은 판정임
기본 너비는 content의 크기임

네비게이션 바같은 효과를 내려면 다음과 같이 사용하면 된다.

	width: 100%;
	position: fixed;
	top: 0;
	left: 0;

그런데 이렇게 사용하면 본문과 네비게이션이 겹칠 수 있다.
body 태그나 본문 태그에 margin을 넣으면 해결될 것이다.


### sticky
일단 기본적으로 원래 있어야할 위치에 배치된다.
fixed처럼 브라우저 화면 기준으로 위치를 정하는데
처음엔 static하게 움직이다가 브라우저 화면 기준으로
설정한 위치에 도달하면 fixed하게 움직인다.
그러다가 기준 밖으로 다시 나가면 원래대로 static으로
전환된다.

sticky는 자리를 차지하는 판정이다

네비게이션 바같은 효과를 내려면 다음과 같이 사용하면 된다.

	width: 100%;
	position: sticky;
	top: 0;
	heigth: 60px;

sticky는 부모 요소 안에 갇혀 있음
즉 부모 요소가 화면 밖에 나가면 자기 자신도 나감


# z-index
코드상 아래에 나오는 요소가 브라우저에선 앞에서 보임
z-index 속성을 설정해주면 나오는 순서를 설정해줄 수 있음

	z-index: 1;

z-index 의 값이 높을수록 더 앞에 있는 요소임

두 요소의 z-index값이 같다면 코드상 아래에 나오는게 앞으로 나옴

모든 정수(음수 양수 0)를 취할 수 있음

### 쌓임 맥락
z-index가 원하는 대로 동작하지 않을 때가 있다.
대부분의 경우는 쌓임 맥락 때문이다.
다음과 같은 예시가 있다고 하자

	<div class="red">
	  <div class="green"></div>
	</div>
	<div class="blue"></div>

	.red {
	  background-color: #e46e80;
	  position: absolute;
	  width: 100px;
	  height: 100px;
	  top: 100px;
	  left: 100px;
	  z-index: 1;
	}

	.green {
	  background-color: #32b9c1;
	  position: absolute;
	  width: 50px;
	  height: 50px;
	  top: 25px;
	  left: 25px;
	  z-index: 3;
	}

	.blue {
	  background-color: #5195ee;
	  position: absolute;
	  width: 100px;
	  height: 100px;
	  top: 150px;
	  left: 150px;
	  z-index: 2;
	}

z-index 순서만 고려한다면 초록 파랑 빨강 순으로 나올 것 같지만
실제론 파랑 초록 빨강 순으로 나온다.
html코드를 확인하면 빨강 div 안에 초록 div가 있다.
따라서 초록 입장에서 관계없는 파랑은 z-index 값을 별개로 적용되는 것이다.
이러한 일련의 맥락을 쌓임 맥락이라고 한다.



# flexbox
flexbox는 일차원 방향으로 배치를 할 때 유용하다
상위 요소에 display:flex를 넣어주면 된다.

	배치할 방향 flex-direction
	정렬하기 justify-content, align-items
	요소가 넘칠 때 flex-wrap
	요소 간격 gap
	크기 늘이거나 줄이기 flex-grow, flex-shrink, flex-basis

### 배치방향
display 속성을 flex로 설정하면
flex-direction 속성의 값이 row로 설정되어 있을 것이다.
가로 방향으로 요소들이 배치되는 것이다

반대로 세로 방향으로 배치하려면
flex-direction 속성의 값을 column 으로 설정해주면 된다.

추가적으로 방향을 반대로 하려면 column-reverse, row-reverse
등을 사용하면 된다.


### 정렬하기
flex-direction 속성으로 요소의 방향을 설정할 수 있다.

### 기본축(Main Axis)
요소가 배치되는 방향

### 교차축(Cross Axis)
기본축에 수직 방향

만약 flex-direction의 값이 column이라면
기본축은 위에서 아래방향이다.

기본적으로 요소들은 기본축 방향으로 순서대로 배치되고
교차축 방향으로 꽉 채워서 배치한다


크롬 개발자 도구에서 display: flex 오른쪽 아이콘을 클릭해보면 
빠르게 설정을 변경할 수 있다.

flex요소에서 다음과 같은 속성을 주로 이용한다.


### flex-direction
위에서 언급했듯이 요소들이 배치되는 방향
아래에서 설명하는 요소들은 flex-direction이 row라고 가정하고 설명했다.

### justify-content
기본축 기준으로 설정

	flex-start: 기본값 가장 왼쪽에 정렬
	flex-right: 가장 오른쪽에 정렬
	center: 가운데 배치
	space-between: 요소마다 간격을 두고 배치
	space-around, space-even: 요소마다 간격을 두고 배치

### align-item
교차축 기준으로 설정

	stretch: 기본값 최대 크기를 차지함
	center: 가운데 정렬, 최대 크기를 차치하는 것이 아닌 
		요소의 크기만큼 공간을 차지함
	flex-end: 맨 아래에 정렬
	flex-start: 맨 위로 정렬


	.trip {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 40px 0 24px;
		padding: 24px 32px;
		border-radius: 8px;
		background: #ebeff8;
	}


### 요소가 넘칠 때
상위 요소의 크기보다 하위 요소들의 크기가 더 커서 넘칠 때,

	flex-wrap: wrap;

를 사용하면 넘치는 요소를 다음 칸으로 넘겨준다.


### 간격
다음과 같은 구조가 있을 때,

```html
<div class="container">
	<div class="red box">RED</div>
	<div class="green box">GREEN</div>
	<div class="blue box">BLUE</div>
</div>
```

간격을 넣으려면

	.box:not(:last-child){
		margin-right: 30px;
	}

이런 식으로 넣어야한다.
gap 속성을 사용하면 다음과 같이 사용할 수 있다.

	.container{
		gap: 30px;
	}

만약 두 줄 이상의 flex 요소를 다뤄야 해서 gap의 가로 새로 크기가
달라야 한다면 다음과 같이 사용할 수 있다.

	.container{
		flex-wrap: wrap
		gap: 30px 60px;
	}

gap 속성의 값은 기본축 교차축 개념없이 무조건 세로 가로 순서로 사용됨
이유는 grid 때문이라고 함


### 요소 꽉 채우기
flex-grow 속성을 사용해서 요소를 꽉 채울 수 있다.
기본적으로 flex-grow를 설정하지 않으면 0을 가지고
양의 정수를 입력하면 그 값에 비례하여 남은 공간을 차지한다.

	.red {
	  background-color: #e46e80;
	}
	
	.green {
	  background-color: #32b9c1;
	  flex-grow:1;
	}
	
	.blue {
	  background-color: #5195ee;
	  flex-grow:2;
	}

flexbox는 하위 요소가 상위 요소의 크기를 넘는 경우
넘어간 크기만큼 비례하여 줄이는 걸 default로 한다.
이러한 특징을 만드는 속성이 flex-shrink다.
기본적으로 모든 flexbox의 기본 flex-shrink 값은 1이고
이 값이 클수록 줄어드는 비율이 늘어 난다.
flex-grow와 반대대는 개념이라고 생각하면 편하다.

대부분의 경우에서 빈공간을 채우고 싶다면 flex-grow:1을 사용하고
크기를 고정하고 싶다면 flex-shrink:0을 사용하면 해결된다.


### flex 요소의 크기
위에서 언급했듯이 flex 요소에선 width와 height로 크기를 설정하였더라도
상위 요소의 크기를 초과하면 알아서 줄어든다.
이 때 기본축에서 설정한 크기를 시작 크기라고 하고,
줄어든 크기를 최종 크기라고 한다.
개발자 도구에서 빗금친 부분이 시작크기이다.
이 때 시작크기를 정할 수 있는 또다른 방법이 flex-basis 속성이다.
그리고 이런 flex-grow, flex-shrink, flex-basis 값을 한 번에 
쓸 수 있는 속성이 flex 속성이다. 아래 3코드는 모드 같은 역할을 한다.

width 속성으로 시작 크기를 지정하기

	flex-grow: 1;
	flex-shrink: 0;
	width: 100px;

flex-basis 속성으로 시작 크기를 지정하기

	flex-grow: 1;
	flex-shrink: 0;
	flex-basis: 100px;

flex 속성으로 짧게 쓰기

	flex: 1 0 100px;


인라인 안에서 flex box만들기
인라인 요소에 flex 같은 효과를 넣으려면 다음과 같이 사용하면 된다

	display: inline-block


### 인라인 안에서 포지셔닝하기
플렉스박스 요소의 포지셔닝을 지정할 수 있다.
absolute와 fixed는 원래 자리를 차지 않고 글의 흐름에서 빠지고
나머지는 포지셔닝을 원래 흐름대로 한다.

```html
<div class="container">
	<div class="red box">RED</div>
	<div class="green box">GREEN</div>
	<div class="blue box">BLUE</div>
</div>
```

	.container {
		border: 5px dashed #cacfd9;
		width: 100%;
		height: 500px;
		display: flex;
		position: relative;
		align-items: flex-start;
	}
	
	.box {
		border-radius: 15px;
		color: #f9fafc;
		padding: 10px;
	}
	
	.red {
		background-color: #e46e80;
	}
	
	.green {
		background-color: #32b9c1;
		flex-grow: 1;
		position: relative;
		top: 100px;
		left: 100px;
	}
	
	.blue {
		background-color: #5195ee;
	}

# Grid
2차원으로 배치함
왼쪽에서 오른쪽으로, 위에서 아래로 배치
각 칸을 나누는 라인을 Grid Line, 요소를 배치할수 있는 공간을 Grid Cell

### Grid 나누기
grid-template-columns, grid-template-rows 속성을 사용해서
grid의 크기를 정할 수 있다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template-columns: 100px 200px 100px;
		grid-template-rows: 200px 200px;
	}

grid-template속성을 사용하여 같은 효과를 낼 수 있다.
아래 코드들은 위의 코드와 동일하다.
row 그다음 column 순서이다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 200px 200px 100px / 100px 200px 100px;
	}

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 
			200px 200px 100px /
			100px 200px 100px;
	}


### 유연한 크기와 유용한 함수들
flexbox처럼 유연하게 크기를 조절하려면 px 대신 fr(fraction)을 사용하면 된다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 
			2fr 2fr 1fr /
			1fr 2fr 1fr;
	}

minmax()로 유연함의 최대와 최소을 설정할 수 있다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 
			2fr 2fr 1fr /
			minmax(100px,200px) minmax(100px,200px) 1fr;
	}

minmax() 안에서도 fr를 사용할 수 있는데, 최대에만 fr을 사용할 수 있다.

fr을 반복해서 사용해야 한다면 repeat()를 사용하여 간단하게 표현할 수 있다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 
			2fr 2fr 1fr /
			repeat(6,1fr);
	}


### 간격 넣기
flex에서 사용했던 gap이랑 완전 동일하게 사용한다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template: 
			2fr 2fr 1fr /
			repeat(6,1fr);
		gap: 16px 32px;
	}


### 크기 미리 정해두기
Grid-Cell 초기값을 설정한다고 생각하면 된다.
아래 코드는 모든 가로 크기를 200px로 바꾸는 코드다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template-columns: repeat(3,1fr);
		grid-auto-rows: 200px; 
		gap: 16px 32px;
	}

아래처럼 번갈아가면서 크기를 사욯할 수도 있다

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template-columns: repeat(3,1fr);
		grid-auto-rows: 50px 100px 200px; 
		gap: 16px 32px;
	}


### 원하는 위치에 요소 배치하기
grid 요소에서 특정 위치에 요소를 배치할 수 있다.
배치하는 방식은 column-line과 row-line을 기준으로 설정할 수 있다.
주의해야할 점은 grid-cell이 아닌 grid-line 기준이다.
grid-row, grid-column 속성을 통해 설정할 수 있다.
음수도 가능하다.

	<div class="container">
		<div class="red box"></div>
		<div class="green box"></div>
		<div class="blue box"></div>
		<div class="purple box"></div>
		<div class="orange box"></div>
	</div>

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template:
			repeat(4, 1fr) /
			repeat(5, 1fr);
		gap: 16px;
	}

	.green {
		grid-row: 3;
		grid-column: 2;
	}

아래는 여러 그리드를 차지하는 방법이다.
column은 3번째에서 4번째까지 row는 1번째에서 4번째까지 영역에 배치
이런 방식으로 위치를 정한다

	.green {
		grid-row: 3 / 5;
		grid-column: 2 / -2;
	}

위에 코드랑 아래는 동일하다.

	.green {
		grid-row: 3 / span 2;
		grid-column: 2 / span 3;
	}


### 이름으로 배치하기
grid-area로 이름을 설정하고, 상위 요소에서 grid-template-areas를
사용해 배치를 할 수 있다.
.을 사용해 빈공간 나타낼 수 있다.

	.container {
		border: 5px dashed #cacfd9;
		width: 500px;
		height: 500px;
		display: grid;
		grid-template:
			repeat(2, 1fr) /
			repeat(2, 1fr);
		gap: 16px;

		grid-template-areas:
			"r g"
			"r b"
			". b";
	}

	.red {
		background-color: #e46e80;
		grid-area: r;
	}

	.green {
		background-color: #32b9c1;
		grid-area: g;
	}

	.blue {
		background-color: #5195ee;
		grid-area: b;
	}



# 반응형 웹
@media
브라우저 크기에 따라 웹디자인을 바꿀 수 있다.

	@media (min-width: 768px){
		h1{
			font-size:36px;
		}
	
		p{
			font-size:24px;
		}
	}