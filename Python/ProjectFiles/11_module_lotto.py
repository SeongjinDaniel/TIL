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
