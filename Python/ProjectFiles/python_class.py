class Dog:
    # MyDogList (파스칼 케이스, upper 카멜 케이스)
    # myDogList (카멜 케이스, lower 카멜 케이스)
    
    kind = 'canine' # 클래스 변수
    
    # 무조건 self가 첫번째 인자로 들어감
    def __init__(self, name):
        self.name = name # 인스턴스 변수

my_dog = Dog('gazi')
your_dog = Dog('namu')

print(my_dog.kind)
print(your_dog.kind)
print(my_dog.name)
print(your_dog.name)

class Dog:
    # tricks = [] # 클래스 변수
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)

my_dog = Dog('gazi')
your_dog = Dog('namu')

my_dog.add_tricks('hello')
your_dog.add_tricks('byebye')

print(my_dog.add_tricks)
print(your_dog.add_tricks)

    


class Dog:
    # tricks = [] # 클래스 변수
    
    def __init__(self, name):
        self.name = name # 인스턴스 변수
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


my_dog = Dog('gazi')
your_dog = Dog('namu')

my_dog.add_tricks('hello')
your_dog.add_tricks('byebye')

print(my_dog.add_tricks)
print(your_dog.add_tricks)


# print(help(str))
# print(help(str.capitalize))

variable = 'apple'

# 단축형
print(variable.capitalize())
# self가 작성되는 이융
print(str.capitalize(variable))


# 절차 지향 vs 객체 지향
# 데이터가 흘러 다니는 것으로 보는 시각 -> 데이터가 중심이 되는 시각

# 절차 지향
# greeting(데이터)
def greeting(name):
    return f'hello, {name}'

print(greeting('harry'))

# 객체 지향
# 데이터.greeting()
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'hello, {self.name}'

my_var = Person('harry')
print(my_var.greeting())

