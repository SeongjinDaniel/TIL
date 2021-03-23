# for문은 정해진 범위 내 시퀀스(문자열, 튜플 리스트 같은)나
# 다른 반복가능한 객체(iterable)의 요소들을 순차적으로 실행합니다.

# 0, 1, 2, 3, 4
for num in [0, 1, 2, 3, 4]:
    print(num)

# 0~99
for num in range(100):
    print(num)

# 1~30중에 짝수인 것들
result = []
for num in range(1, 31):
    if num % 2 == 0:
        result.append(num)
print(result)

lunch = ['짜장면', '초밥', '탕수육']
for index,  menu in enumerate(lunch):
    print(index, menu)

print(enumerate(lunch))
print(type(enumerate(lunch)))
print(list(enumerate(lunch))) # list 내부는 tuple!!
print(type(list(enumerate(lunch))[0]))