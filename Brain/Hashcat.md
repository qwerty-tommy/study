# 용도
hash를 크랙해주는 툴

https://www.onlinehashcrack.com/hashes
이런 온라인툴과 유사함

# 사용법

	hashcat -a 3 -m 0 hash.txt ?d?d?d?d

-a 알고리즘	3이면 md5
-m 모드	0이면 파일(리스트)에있는거 넣어보는 straight
?d~	정규표현식같은 표현식

자세한건 

	hashcat --help