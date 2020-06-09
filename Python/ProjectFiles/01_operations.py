# 논리 연산자
print('--- and ---')
print(True and True)
print(True and False)
print(True and False)
print(False and False)

# ctrl + d 단축키 : 하단으로 같은 단어들을 동시에 선택 할 수 있다.
print('--- or ---')
print(True or True)
print(True or False)
print(True or False)
print(False or False)

print('--- not ---')
print(not True)
print(not 0)

# 단축평가
# 첫번째 값이 확실할 때, 두번째 값은 확인하지 않음
# 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상
print('--- 단축평가 ---')
vowels = 'aeiou'
print(('a' and 'b') in vowels) # False
print(('b' and 'a') in vowels) # True
print('a' and 'b') # 'b' 뒤에꺼 까지 봐야한다. a가 True라고 해서 뒤에께 True라는 보장이 없으니까

# and는 둘 다 True 경우만 True이기 때문에
# 첫번째 값이 True라도 두번째 값을 확인해야 한다.
print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

# true는 첫번째 true이면 뒤에꺼를 볼필요가 없다.
print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0

# Containment Test
# in 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.

print('--- in ---')
print('a' in 'apple')
print(1 in [1, 2, 3]) # 파이썬은 Array를 List라고 부른다.
