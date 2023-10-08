# 비트 연산 중 조심할 것
16*j와 j << 4 는 기본적으로 비슷한 연산이다.

리버싱을 하다보면
L-shift를 하는 일이 생길건데,
만약 4비트 L-shift해야한다면 코드 작성할 때
(j << 4) & 0xF0 이런 식으로
자료형의 크기를 유지시켜줘야한다.

# XOR
xor을 두번 연산하면 자기 자신이 나오기 때문에
암호화한 척하기 좋은 로직이다.

# 홀수짝수판별
    and eax 0x1
    test eax eax

# tip
리버싱 특성상 새로운 환경을 자주 만난다
모르는 건 항상 구글링..