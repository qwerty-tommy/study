# 컴퓨터공학부 전용 수강신청 메크로

### 실행

1. 파이썬 설치
2. pip로 main.py 상단 주석에 dependency 모두 설치
3. /src/main.py 에서 로그인 정보 수정(user_id, user_pw)
4. 신청하고 싶은 과목 리스트 추가(wishlist)
5. `python main.py`로 실행

### 기능

- ~~소망가방 초과인원 정보 제공(예정)~~
- 시간표 결정 관련 정보 제공
- 수강신청, 소망가방신청 메크로
- 소망가방 초기화

### 사용법

- 설정 제대로 했으면 시작하자마자 세션연결 완료됨
- 1번으로 사용중인 세션 아이디 확인 가능
- 2번으로 로컬로 신청 관련 모든 데이터를 가져옴
- 3번으로 2번에서 가저온 데이터, 위시리스트 기반으로 가능한 모든 시간표를 10개씩 보여주고 결정할 수 있음
- 4번으로 3번에서 결정된 시간표를 한번에 신청할 수 있음
- 5번으로 소망가방을 초기화할 수 있음
- ~~6번으로 3번에서 결정된 시간표를 한번에 신청할 수 있음(더 빠르게 하려면 3번에서 초과된거 제외하고 신청하고, 멀티쓰레드로 동시에 패킷보내면 베스트)~~
- 모든 수강 신청 정보를 `/src/full_data`에서 csv 형태로 직접 확인할 수 있음
- 사용자가 선택한 정보를 `/src/target_data`에서 csv 형태로 직접 확인할 수 있음
- 프로그램 실행 중에 브라우저에 직접 세션을 변조해서 프로그램 실행 결과를 실시간으로 확인할 수 있음

### 주의사항

- 컴퓨터공학부에서만 테스트 해봤음 -> 다른 학과에서는 어느 정도 수정해서는 안될 수도 있음
- 특정 과목은 새로운 파라미터를 요구하는 것을 확인했음 -> 코드 직접 수정해야 함
- 모든 조합을 확인하기 때문에 과목수가 너무 많으면 복잡도 이슈로 너무 오래 걸릴 수도 있음
- `/src` 로 이동 후 실행해야 함
- 아직 개발 중
