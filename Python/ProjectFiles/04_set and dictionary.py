# 1. set 집합!!!!  순서없음!!
set_a = {1, 2, 3}
set_b = {3, 6, 9}

print(set_a - set_b) # 차집합
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

set_c = set() # 빈 set를 만들 때 {}를 사용하면 dict이기때문에 클래스 객체를 사용한다.(어쩔수 없이...)

# 중복 허용 x
set_temp = {1, 1, 1} # => {1}
print(set_temp)

# 2. dictionary   --> 궁극의 자료구조!!
dict_a = {} # 괄호를 사용해서 호출하면 훨씬더 메모리를 줄여서 사용할 수 있다.
print(type(dict_a))
dict_b = dict()
print(type(dict_b))
# key:value
dict_a = {1: 1, 2: 2, 3: 3, 1: 4} # key가 중복됨
print(dict_a)

# json 구조와 같다!
phone_book = {
    '서울': '02',
    '경기': '031',
    '대전': '042'
}
print(phone_book['서울'])

print(dir(dict)) # dir을 사용하면 어떤 함수를 사용할 수 있는지 알 수 있다.

# phone_book. 이렇게 치면 나오는 함수들을 확인 할 수 있다.
print(phone_book.values()) # dict_values(['02', '031', '042']) ---> 딱 값들만 나옴! 대괄호로 감싸져 있으니 list네!!! wow!
# dictionary는 만들때 그순서는 보장해주지만 set은 보장 x
# print(help(dict)) 

