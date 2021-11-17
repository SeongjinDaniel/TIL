# Redis Command 정리



#### SET

key, value를 설정할 수 있다. 키에 이미 값이 있으면 유형에 관계없이 덮어쓴다.

https://redis.io/commands/set



#### Exsits

key가 있으면 반환합니다. Redis 3.0.3부터 단일 키 대신 여러 키를 지정할 수 있다.

- `1` if the key exists.
- `0` if the key does not exist.

```
redis> SET key1 "Hello"
"OK"
redis> EXISTS key1
(integer) 1
redis> EXISTS nosuchkey
(integer) 0
redis> SET key2 "World"
"OK"
redis> EXISTS key1 key2 nosuchkey
(integer) 2
```



#### GET

key값을 가져온다. 키가 존재하지 않으면 특수 값 nil이 반환된다. GET은 문자열 값만 처리하므로 key에 저장된 값이 문자열이 아닌 경우 오류가 반환된다.

```
redis> GET nonexisting
(nil)
redis> SET mykey "Hello"
"OK"
redis> GET mykey
"Hello"
```



#### DEL

지정된 키를 제거합니다. 키가 존재하지 않으면 무시된다.

```
redis> SET key1 "Hello"
"OK"
redis> SET key2 "World"
"OK"
redis> DEL key1 key2 key3
(integer) 2
```



#### INCRBY

키에 저장된 숫자를 증분으로 증가. 키가 존재하지 않으면 작업을 수행하기 전에 0으로 설정된다. 키에 잘못된 유형의 값이 포함되어 있거나 정수로 나타낼 수 없는 문자열이 포함되어 있으면 오류가 반환된다. 이 작업은 64비트 signed Integer로 제한된다.

```
redis> SET mykey "10"
"OK"
redis> INCRBY mykey 5
(integer) 15
```



#### DECRBY

키에 저장된 숫자를 감소시킨다. 키가 존재하지 않으면 작업을 수행하기 전에 0으로 설정됩니다. 키에 잘못된 유형의 값이 포함되어 있거나 정수로 나타낼 수 없는 문자열이 포함되어 있으면 오류가 반환된다. 이 작업은 64비트 signed Integer로 제한된다.

```
redis> SET mykey "10"
"OK"
redis> DECRBY mykey 3
(integer) 7
```



#### ZREMRANGEBYSCORE

최소에서 최대(포함) 사이의 점수로 key에 저장된 정렬된 세트의 모든 요소를 제거한다.

반환 값은 제거된 수이다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREMRANGEBYSCORE myzset -inf (2
(integer) 1
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "two"
2) "2"
3) "three"
4) "3"
```



#### ZADD

key에 저장된 정렬된 집합에 지정된 scores를 가진 지정된 모든 멤버를 추가한다. 여러 scores/members 쌍을 지정할 수 있다. 지정된 구성원이 이미 정렬된 집합의 구성원인 경우 scores가 업데이트되고 올바른 순서를 보장하기 위해 요소가 올바른 위치에 다시 삽입된다. 

키가 없으면 정렬된 집합이 비어 있는 것처럼 지정된 members 을 단독 members으로 사용하여 새 정렬된 집합이 생성된다. 키가 있지만 정렬된 집합이 없으면 오류가 반환된다.

scores 값은 배정밀도 부동 소수점 숫자의 문자열 표현이어야 합니다. +inf 및 -inf 값도 유효한 값입니다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 1 "uno"
(integer) 1
redis> ZADD myzset 2 "two" 3 "three"
(integer) 2
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "one"
2) "1"
3) "uno"
4) "1"
5) "two"
6) "2"
7) "three"
8) "3"
```



#### ZREM

key에 저장된 정렬된 집합에서 지정된 멤버를 제거한다. 존재하지 않는 구성원은 무시된다. 키가 존재하고 정렬된 집합을 보유하지 않으면 오류가 반환된다.

```
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREM myzset "two"
(integer) 1
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "one"
2) "1"
3) "three"
4) "3"
```



#### ZINCRBY

키에 저장된 정렬된 집합의 멤버 score를 증분으로 늘린다. 정렬된 집합에 구성원이 없으면 score가 증가하여 추가된다(이전 점수가 0.0인 것처럼). 키가 없으면 지정된 멤버를 유일한 멤버로 사용하여 새로운 정렬된 세트가 생성된다. 

키가 있지만 정렬된 집합을 보유하지 않으면 오류가 반환됩니다. score 값은 숫자 값의 문자열 표현이어야 하며 배정밀도 부동 소수점 숫자를 허용합니다. score를 낮추기 위해 음수 값을 제공할 수 있습니다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZINCRBY myzset 2 "one"
"3"
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "two"
2) "2"
3) "one"
4) "3"
```



#### ZCARD

key에 저장된 정렬된 집합의 정렬된 집합 카디널리티(요소의 수)를 반환한다.

반환: 정렬된 집합의 카디널리티(요소 수) 또는 키가 없으면 0이다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZCARD myzset
(integer) 2
```



#### ZRANK

key에 저장된 정렬된 집합의 구성원 순위를 낮은 것에서 높은 순서로 score와 함께 반환한다. 순위(또는 인덱스)는 0부터 시작한다. 즉, 점수가 가장 낮은 멤버의 순위가 0이다.

ZREVRANK를 사용하여 높은 score에서 낮은 score 순서로 요소의 순위를 가져온다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZRANK myzset "three"
(integer) 2
redis> ZRANK myzset "four"
(nil)
```



#### ZREVRANK

키에 저장된 정렬된 집합의 구성원 순위를 높은 score에서 낮은score 순서로 반환합니다. 순위(또는 인덱스)는 0부터 시작하므로 점수가 가장 높은 멤버의 순위가 0입니다.

ZRANK를 사용하여 낮은 점수에서 높은 점수 순서로 요소의 순위를 가져온다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREVRANK myzset "one"
(integer) 2
redis> ZREVRANK myzset "four"
(nil)
```



#### ZSCORE

키의 정렬된 집합에서 멤버의 점수를 반환한다. 정렬된 집합에 멤버가 없거나 키가 없으면 nil이 반환된다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZSCORE myzset "one"
"1"
```



#### ZCOUNT

최소와 최대 사이의 점수를 가진 정렬된 집합의 element의 수를 key에서 반환한다. min 및 max 인수는 ZRANGEBYSCORE에 대해 설명한 것과 동일한 의미를 갖습니다.

이 명령은 범위에 대한 아이디어를 얻기 위해 요소 순위(ZRANK 참조)를 사용하기 때문에 복잡도가 O(log(N))에 불과하다. 이 때문에 범위의 크기에 비례하는 작업을 할 필요가 없다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZCOUNT myzset -inf +inf
(integer) 3
redis> ZCOUNT myzset (1 3
(integer) 2
```



#### ZREVRANGE

key에 저장된 정렬된 집합에서 지정된 범위의 요소를 반환한다. 요소는 가장 높은 점수에서 가장 낮은 점수 순으로 정렬된 것으로 간주된다. 내림차순 사전순은 점수가 같은 요소에 사용된다.

역순을 제외하고 ZREVRANGE는 ZRANGE와 유사하다. Redis 6.2.0에 따라 이 명령은 더 이상 사용되지 않는 것으로 간주된다. 새 코드에서 REV 인수와 함께 ZRANGE 명령을 사용하는 것을 선호해야한다.

```
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREVRANGE myzset 0 -1
1) "three"
2) "two"
3) "one"
redis> ZREVRANGE myzset 2 3
1) "one"
redis> ZREVRANGE myzset -2 -1
1) "two"
2) "one"
```



#### ZRANGEBYSCORE

최소와 최대 사이의 점수를 가진 정렬된 키의 모든 요소를 반환한다(최소 또는 최대와 같은 점수를 가진 요소 포함). 요소는 낮은 점수에서 높은 점수로 정렬된 것으로 간주된다. 

동일한 점수를 가진 요소는 사전순으로 반환된다(이는 Redis의 정렬된 집합 구현 속성에서 따르며 추가 계산을 포함하지 않음).

Redis 6.2.0에 따라 이 명령은 더 이상 사용되지 않는 것으로 간주된다. 새 코드에서 BYSCORE 인수와 함께 ZRANGE 명령을 사용하는 것을 선호해야한다.

선택적 LIMIT 인수는 일치하는 요소의 범위만 가져오는 데 사용할 수 있습니다(SQL의 SELECT LIMIT 오프셋, 개수와 유사). 음수 개수는 오프셋의 모든 요소를 반환한다. 오프셋이 크면 반환할 요소에 도달하기 전에 오프셋 요소에 대해 정렬된 세트를 순회해야 하므로 O(N) 시간 복잡도가 추가될 수 있습니다.

`ZRANGEBYSCORE zset (1 5`

Will return all elements with 1 < score <= 5 while:

`ZRANGEBYSCORE zset (5 (10`

Will return all the elements with 5 < score < 10 (5 and 10 excluded).

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZRANGEBYSCORE myzset -inf +inf
1) "one"
2) "two"
3) "three"
redis> ZRANGEBYSCORE myzset 1 2
1) "one"
2) "two"
redis> ZRANGEBYSCORE myzset (1 2
1) "two"
redis> ZRANGEBYSCORE myzset (1 (2
(empty list or set)
```



#### ZREVRANGEBYSCORE

점수가 max와 min 사이인 key at 정렬된 집합의 모든 요소를 반환한다(점수가 max 또는 min과 같은 요소 포함). 정렬된 세트의 기본 순서와 달리 이 명령의 경우 요소는 높은 점수에서 낮은 점수로 정렬된 것으로 간주된다.

동일한 점수를 가진 요소는 사전순 역순으로 반환된다.

역순을 제외하고 ZREVRANGEBYSCORE는 ZRANGEBYSCORE와 유사합니다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREVRANGEBYSCORE myzset +inf -inf
1) "three"
2) "two"
3) "one"
redis> ZREVRANGEBYSCORE myzset 2 1
1) "two"
2) "one"
redis> ZREVRANGEBYSCORE myzset 2 (1
1) "two"
redis> ZREVRANGEBYSCORE myzset (2 (1
(empty list or set)
```



#### ZRANGE

<key>에 저장된 정렬된 집합에서 지정된 요소 범위를 반환한다. ZRANGE는 인덱스(순위), 점수 또는 사전순과 같이 다양한 유형의 범위 쿼리를 수행할 수 있다.

Redis 6.2.0부터 이 명령은 ZREVRANGE, ZRANGEBYSCORE, ZREVRANGEBYSCORE, ZRANGEBYLEX 및 ZREVRANGEBYLEX 명령을 대체할 수 있다.

```
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZRANGE myzset 0 -1
1) "one"
2) "two"
3) "three"
redis> ZRANGE myzset 2 3
1) "three"
redis> ZRANGE myzset -2 -1
1) "two"
2) "three"
```

```
redis> ZRANGE myzset 0 1 WITHSCORES
1) "one"
2) "1"
3) "two"
4) "2"
```

```
redis> ZRANGE myzset (1 +inf BYSCORE LIMIT 1 1
1) "three"
```



#### SADD

key에 저장된 집합에 지정된 멤버를 추가한다. 이미 이 집합의 구성원인 지정된 구성원은 무시된다. 키가 없으면 지정된 구성원을 추가하기 전에 새 집합이 생성된다.

key에 저장된 값이 set이 아닐 경우 error를 반환한다.

```
redis> SADD myset "Hello"
(integer) 1
redis> SADD myset "World"
(integer) 1
redis> SADD myset "World"
(integer) 0
redis> SMEMBERS myset
1) "World"
2) "Hello"
```



#### SISMEMBER

구성원이 키에 저장된 집합의 구성원인 경우 반환한다.

- 요소가 집합의 구성원인 경우 1이다. 
- 요소가 집합의 구성원이 아니거나 키가 존재하지 않는 경우 0이다.

```
redis> SADD myset "one"
(integer) 1
redis> SISMEMBER myset "one"
(integer) 1
redis> SISMEMBER myset "two"
(integer) 0
```



#### SMEMBERS

키에 저장된 설정 값의 모든 멤버를 반환한다. 이것은 하나의 인수 키로 [SINTER](https://redis.io/commands/sinter)를 실행하는 것과 같은 효과를 가진다.

```
redis> SADD myset "Hello"
(integer) 1
redis> SADD myset "World"
(integer) 1
redis> SMEMBERS myset
1) "World"
2) "Hello"
```



#### SREM

key에 저장된 집합에서 지정된 멤버를 제거한다. 이 집합의 구성원이 아닌 지정된 구성원은 무시된다. 키가 없으면 빈 집합으로 처리되고 이 명령은 0을 반환한다. key에 저장된 값이 set이 아닐 경우 error를 반환한다.

```
redis> SADD myset "one"
(integer) 1
redis> SADD myset "two"
(integer) 1
redis> SADD myset "three"
(integer) 1
redis> SREM myset "one"
(integer) 1
redis> SREM myset "four"
(integer) 0
redis> SMEMBERS myset
1) "three"
2) "two"
```



#### SPOP

집합에서 무작위로 member를 가져옴.

키의 설정 값 저장소에서 하나 이상의 임의 멤버를 제거하고 반환한다.

이 작업은 집합에서 하나 이상의 임의 요소를 반환하지만 제거하지는 않는 SRANDMEMBER와 유사하다.

기본적으로 이 명령은 집합에서 단일 구성원을 팝합니다. 선택적 count 인수와 함께 제공되면 응답은 집합의 카디널리티에 따라 최대 count 멤버로 구성된다.

```
redis> SADD myset "one"
(integer) 1
redis> SADD myset "two"
(integer) 1
redis> SADD myset "three"
(integer) 1
redis> SPOP myset
"one"
redis> SMEMBERS myset
1) "three"
2) "two"
redis> SADD myset "four"
(integer) 1
redis> SADD myset "five"
(integer) 1
redis> SPOP myset 3
1) "three"
2) "four"
3) "two"
redis> SMEMBERS myset
1) "five"
```



#### SRANDMEMBER

SPOP은 조회하고 데이터를 삭제하는데, 이 명령은 조회만한다.

key 인수만으로 호출하면 key에 저장된 설정 값에서 임의의 요소를 반환한다. 제공된 count 인수가 양수이면 고유한 요소의 배열을 반환한다. array의 길이는 개수 또는 세트의 카디널리티(SCARD) 중 더 작은 것이다.

음수 카운트로 호출하면 동작이 변경되고 명령이 동일한 요소를 여러 번 반환할 수 있습니다. 이 경우 반환되는 요소의 개수는 지정된 개수의 절대값입니다.

```
redis> SADD myset one two three
(integer) 3
redis> SRANDMEMBER myset
"two"
redis> SRANDMEMBER myset 2
1) "three"
2) "two"
redis> SRANDMEMBER myset -5
1) "one"
2) "three"
3) "one"
4) "two"
5) "two"
```



#### HEXISTS

필드가 키에 저장된 해시의 기존 필드인 경우 반환한다.

- 해시에 필드가 포함된 경우 1이다.
-  해시에 필드가 없거나 키가 없는 경우 0이다.

```
redis> HSET myhash field1 "foo"
(integer) 1
redis> HEXISTS myhash field1
(integer) 1
redis> HEXISTS myhash field2
(integer) 0
```

