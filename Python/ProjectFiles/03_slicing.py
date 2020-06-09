# 파이썬에서는 변수명이나 함수명을 snake case를 사용한다.
sample_list = list(range(0, 31))
print(sample_list)
print(sample_list[1:3]) # : 이 슬라이싱!! 공간으로 자른다!
print(sample_list[10:-1]) # 끝에것만 제거 ! <---- -2, -1, 0   <----
print(sample_list[0 : len(sample_list) : 3])
print(sample_list[0::3]) # 위와 같음!
print(sample_list[::3]) # 위와 같음!

print(sample_list[::-1]) # 역순으로 !! 회문에서 사용!
print(sample_list[1:1]) # 아무것도 없음!! slcing을 어떻게 짜른지 생각하면 알수 있음!!