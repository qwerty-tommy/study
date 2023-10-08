# 리다이렉션(>)
cat은 일반적으로 cat 명령어 다음 입력한 내용을 모니터로
출력해주는 기능을 한다. 그러나

	cat > tmp.txt

이런 식으로 리다이렉션을 사용하면 입력한 내용을 tmp.txt로
'방향을 바꿔' 출력한다.

추가적으로 리다이렉션 을 두 번 사용하면 append 효과가 난다

	cat  >> tmp.txt
	
&>/dev/null: 모든 출력을 /dev/null로 리다이렉션하여 출력을 무시


# 압축
보통 songs.tar.gz 이런 식으로 되어있는데
먼저 gzip을 풀어서 songs.tar로 만드고
그 tar를 해제해서 songs를 사용하면 된다.

### tar
tar는 그냥 합치기만 그래서 오히려 용량이 늘어남 속도가 빠른편

	tar cvf songs.tar *		압축
	tar xvf songs.tar		해제
### gzip
실제로 압축하는 명령어

	gzip 파일이름		선택된 파일을 압축
	gzip -d 파일이름	선택된 파일을 해제
### 확장자	
tar		
tar 프로그램을 사용하여 압축된 파일,
사실 압축이 아닌 여러 파일들이 하나로 뭉쳐져 있는 파일

gz 
gzip 프로그램을 사용하여 압축된 파일

tar.gz	
tar 프로그램을 사용하여 파일을 합친 후, 또 다시 gzip 을 사용하여 압축을 한 파일

tgz
위의 tar.gz 을 합쳐서 tgz라는 확장자로 만듬

# 주요 리눅스 디렉토리 구조	

bin		필수적인 리눅스 실행 파일이 들어가있는 디렉토리
boot	부팅관련 파일, 그리고 커널이 들어있는 디렉토리
dev		컴퓨터에 설치된 하드웨어에 관한 정보들이 파일 형태로 저장되어 있는 디렉토리
etc		많은 중요한 파일들이 들어있는 디렉토리 패스워드 파일, 쉐도우 파일, 대부분의 리눅스 설정 파일
home	일반 사용자들의 홈 디렉토리
lib		라이브러리 파일들이 들어가있는 디렉토리
mnt	mount 명령을 통해 마운트 시킨 시디룸, 플로피 드스켓 등이 들어가있는 디렉토리			
proc	프로세스들이 파일 형태로 저장된는 디렉토리
root	root의 홈 디렉토리
sbin	기본 명령을 제외한 시스템 관리용 실행 파일이 들어가 있는 디렉토리
tmp		임시로 파일을 저장하는 디렉토리, 권환 상관없이 누구나 파일을 생성할 수 있음
usr		다양한 응용 프로그램들이 설치되어 있는 곳
var		시스템 운영 중 생성되는 임시 파일들이 들어가 있는 디렉토리 외부 접속에 대한 로그 파일들이 이 곳에 저장됨
	

# 리눅스에서 중요한 역할을 하는 것들

/etc/passwd		사용자들에 대한 간단한 정보가 들어있음
/etc/shadow		사용자들의 패스워드
/etc/services	서버가 어떤 서비스를 하는지 확인할 수 있음
/etc/issue.net	처음 접속될 때 나오는 화면
/etc/motd		로그인 후에 나오는 메세지
~/public_html	각 사용자의 홈페이지 파일, 보통 해킹 후 수정함


# 모니터링 명령어

프로세스 확인
	ps 		현재 실행중인 프로세스 목록
	top		시스템 리소스 사용량 모니터링 + 실행 프로세스
	htop 	top보다 더 많은 정보
	pgrep [프로세스 이름]		특정 이름을 가진 프로세스의 PID 검색

네트워크 확인
	lsof -i :7000	해당 포트에 있는 서비스 확인
	kill -9 5710	서비스 죽이기
	netstat -ano	모든 포트에서 사용하는 프로세스 확인	

# scp
	scp -p 5022 Foo1@211.250.216.249:/root/rv-sh /root/


# tty를 이용한 쉘 업그레이드
리눅스에선 사용자마다 임시 터미널을 받음 해당 터미널을 식별할때 사용

	qwertyou@DESKTOP-8HVF2JQ:~$ tty
	/dev/pts/0


# 설치 스크립트
한글 폰트

chrome

	wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
	sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
	sudo apt update
	sudo apt install google-chrome-stable

apm

	sudo apt update & sudo apt upgrade -y
	sudo apt install apache2 php php-mysql mysql-server -y
	sudo service apache2 start

docker

	sudo apt update
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt install docker-ce
	sudo systemctl start docker
	sudo systemctl enable docker
	sudo usermod -aG docker $USER

docker-compose

	sudo apt update
	sudo apt install docker-compose
	docker-compose --version

네트워크툴

	apt install net-tools

vim

	apt install vim

ssh

	sudo apt-get update
	sudo apt-get install openssh-server


# 공개키 오류

키 다시 받기
	wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -

키 추가하기
	sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5