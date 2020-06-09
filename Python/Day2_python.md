# 모듈 / 함수 / 라이브러리 (공적마스크 api)

**random 공식문서 url**

https://docs.python.org/ko/3.7/library/random.html



## Functions for sequences

- `random.choice`(*seq*)

  Return a random element from the non-empty sequence *seq*. If *seq* is empty, raises [`IndexError`](https://docs.python.org/ko/3.7/library/exceptions.html#IndexError).

- `random.``sample`(*population*, *k*)

  Return a *k* length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.

  Returns a new list containing elements from the population while leaving the original population unchanged. The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).

  Members of the population need not be [hashable](https://docs.python.org/ko/3.7/glossary.html#term-hashable) or unique. If the population contains repeats, then each occurrence is a possible selection in the sample.

  To choose a sample from a range of integers, use a [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range) object as an argument. This is especially fast and space efficient for sampling from a large population: `sample(range(10000000), k=60)`.

  If the sample size is larger than the population size, a [`ValueError`](https://docs.python.org/ko/3.7/library/exceptions.html#ValueError) is raised.

- `random.``randrange`(*stop*)

  `random.``randrange`(*start*, *stop*[, *step*])

  Return a randomly selected element from `range(start, stop, step)`. This is equivalent to `choice(range(start, stop, step))`, but doesn’t actually build a range object.

  The positional argument pattern matches that of [`range()`](https://docs.python.org/ko/3.7/library/stdtypes.html#range). Keyword arguments should not be used because the function may use them in unexpected ways.

  *버전 3.2에서 변경:* [`randrange()`](https://docs.python.org/ko/3.7/library/random.html#random.randrange) is more sophisticated about producing equally distributed values. Formerly it used a style like `int(random()*n)` which could produce slightly uneven distributions.



##### 10_module_radom.py

```python
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


```



##### 11_module_lotto.py

```python
import random # 내부 모듈
# pip install requests를 terminal에서 사용하여 requests 모듈을 설치한다!!
import requests # 크롤링하기 위함 !!(내부 모듈 x -> 설치 해야함)

numbers = range(1, 46)
print(list(numbers))
print('-----lotto-----')
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
# print(response) # <Response [200]> -> 객체
# print(dir(response))
# print(response.content) # json형식!
# print(response.json()) # json형식이 아니고dict형식이다.
lotto_info = response.json()
print(lotto_info)

# key가 없으면 KeyError: 'bonusNo'
bonus_num = lotto_info['bnusNo']
# key가 없으면 None으로 처리가 된다. !! 
bonus_num = lotto_info.get('bnusNo')
print(bonus_num)

winner = []

for i in range(1,7):
    tmpKey = lotto_info.get(f'drwtNo{i}')
    winner.append(tmpKey)

# pick, winner 비교
bonus = lotto_info.get('bnusNo')
count = 0
bnusCount = 0
# print(list(range(7)))
for i in list(range(0, 6)):
    for j in range(0, 6):
        if pick[i] == winner[j]:
            count = count + 1
        elif pick[i] == bonus:
            bnusCount = bnusCount + 1

print(winner)
print(pick)
if count == 6:
    print('Lotto 1등 당첨!!')
elif count == 5 and bnusCount == 1:
    print('Lotto 2등 당첨!!')
elif count == 5:
    print('Lotto 3등 당첨!!')
elif count == 4:
    print('Lotto 4등 당첨!!')
elif count == 3:
    print('Lotto 5등 당첨!!')
else:
    print('다음 기회에!!')
    
# 강사님!!!!!!!!!!!!!!!!!!!!코드!!!!!!!!!!!!!!!!!!!
match_num = set(pick) & set(winner)
print(match_num) # 중복숫자 출력됨
print(len(match_num)) # 숫자 값 나옴!

```



json은 "" 쌍따옴표로 써야 json이다!!!!!!!!!!!

크롬에서 json viewer 확장프로그램을 설치하면 더 쉽게 볼수 있다.



##### 12_my_mask.py

```python
import requests
from pprint import pprint
URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

params = '?address=서울특별시 강남구 역삼동'

response = requests.get(URL+params)
# print(URL + params)
stores = response.json().get('stores')[:10] # [:10] 처음부터 10개만 뽑아옴
# print(stores)

for store in stores:
    # pprint(store)
    # print(store.get('name'))
    name = store.get('name')
    remain = store.get('remain_stat')
    if remain == 'plenty':
        color = 'green'
    elif remain == 'some':
        color = 'yellow'
    elif remain == 'few':
        color = 'red'
    elif remain == 'empty':
        color = 'grey'
    else:
        color = '판매중지'

    print(store.get('name') + ' ' + color)


```



##### 13_function.py

```python
# 정의
def hello():
    print('hihi')

# 사용
hello()

def add(a, b):
    return a + b

result = add(1, 2)
print(result)

```



#### 14_my_function.py

```python
from public import public_mask

public_mask.mask('서울특별시 강남구 역삼동')
```

밑에 파일을 읽어와서 사용함!!!

##### public 폴더 안에 public_mask.py

```python
import requests
from pprint import pprint

def mask(address, n=10):
    # print(address, n)
    params = '?address=서울특별시 강남구 역삼동'
    URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
    response = requests.get(URL+params)
    # print(URL + params)
    stores = response.json().get('stores')[:n] # [:10] 처음부터 10개만 뽑아옴
    # print(stores)

    for store in stores:
        # pprint(store)
        # print(store.get('name'))
        remain = store.get('remain_stat')
        if remain == 'plenty':
            color = 'green'
        elif remain == 'some':
            color = 'yellow'
        elif remain == 'few':
            color = 'red'
        elif remain == 'empty':
            color = 'grey'
        else:
            color = '판매중지'

        print(store.get('name') + ' ' + color)


mask('서울특별시 강남구', 20)
```



