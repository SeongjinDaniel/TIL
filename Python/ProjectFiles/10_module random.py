import random

numbers = [1, 2, 3, 4, 5]
result = random.choice(numbers)
print(result)

pick = random.choice(range(10))
print(pick)

# 0~19까지 3개를 보여준다.
n = random.sample(range(20), 3)
print(n)

# random이 가지고 있는 기능들의 함수
print(dir(random))

