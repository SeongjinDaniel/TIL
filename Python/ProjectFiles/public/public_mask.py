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
