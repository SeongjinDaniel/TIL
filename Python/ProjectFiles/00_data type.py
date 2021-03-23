print('Hello, World')

number = 10
string = '문자열'
bools = True

print(number, string, bools)

# 주석

# 숫자형 (int, float, complex)
a = 3
print(type(a))

# bool
print(type(False))

# 0, 0.0, (), [], {}, '', None -> 얘네는 False

# 문자형
greeting = 'hi'
name = 'harry'
print(greeting, name)
print(type(name))

# 사용자의 입력을 받음
# age = input()
# 사용자의 모든 입력 값은 string이어서 정수형을 쓰려면 변경해서 사용해야한다.
# print(type(age))

print("""
개행 문자 없이
여러줄을
그대로 출력 가능합니다.
""")

print(3 * 'hey' + ' yo!')

# string interpoltion

name = 'kim'
# 1. %-formatting
print('Hello, %s' % name)
# 2. .format()
print('Hello, {}'.format(name))
# 3. f-string (Literal String Interpolation) / 3.6+
print(f'Hello, {name}') # 소문자로 사용!!

pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2:.4}')

