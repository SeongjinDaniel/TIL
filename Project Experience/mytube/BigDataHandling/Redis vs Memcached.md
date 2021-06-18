# Redis vs Memcached



**Redis와 Memcached 어떤걸 사용해야 할까요?**

![image](https://user-images.githubusercontent.com/55625864/93844408-05489600-fcd8-11ea-9a6f-f235ee946f3b.png)

​																					DB-Engines Ranking

[DB-Engines Ranking](https://db-engines.com/en/ranking)은 인기도에 따라 데이터베이스 관리 시스템의 순위를 나타냅니다. 현재는 Redis가 7위 Memcached가 27위 입니다.(2020.09.22 기준)

![image](https://user-images.githubusercontent.com/55625864/93845668-a1749c00-fcdc-11ea-9154-46dfaf1bf258.png)



위 그래프는 인기도에 따라 데이터베이스 관리 시스템의 순위를 나타냅니다.

이것만 봐도 대부분의 개발자들이 Redis를 월등히 많이 사용하고 있다는것을 알 수 있고 둘중에 하나를 선택하라면 당연히 저는 Redis를 사용할 것 같습니다.



하지만 저렇게 순위가 높고 많이 사용한다고 해서 저것을 택해야한다기 보다는 좀더 자세한 둘의 차이점과 장단점을 비교해서 알아보겠습니다.



위키에 따르면 레디스는

> **레디스**(Redis)는 Remote Dictionary Server의 약자로서, "키-값" 구조의 비정형 데이터를 저장하고 관리하기 위한 [오픈 소스](https://ko.wikipedia.org/wiki/오픈_소스) 기반의 비관계형 [데이터베이스 관리 시스템](https://ko.wikipedia.org/wiki/데이터베이스_관리_시스템)(DBMS)입니다. 2009년 [살바토르 산필리포](https://ko.wikipedia.org/w/index.php?title=살바토르_산필리포&action=edit&redlink=1)(Salvatore Sanfilippo)가 처음 개발했습니다.

위키에 따르면 Memcached는

> **Memcached** (멤캐시디, 멤캐시트)는 범용 분산 [캐시](https://ko.wikipedia.org/wiki/캐시) 시스템입니다. 외부 데이터 소스(예: 데이터베이스나 API)의 읽기 횟수를 줄이기 위해 데이터와 [객체](https://ko.wikipedia.org/wiki/객체_(컴퓨터_과학))들을 [RAM](https://ko.wikipedia.org/wiki/랜덤_액세스_메모리)에 캐시 처리함으로써 동적 [데이터베이스](https://ko.wikipedia.org/wiki/데이터베이스) 드리븐 웹사이트의 속도를 높이기 위해 종종 사용됩니다.
>
> Memcached는 2003년 5월 22일 [Brad Fitzpatrick](https://ko.wikipedia.org/w/index.php?title=Brad_Fitzpatrick&action=edit&redlink=1)가 자신의 웹사이트 [라이브저널](https://ko.wikipedia.org/wiki/라이브저널)을 위해 처음 개발한 것입니다.



위와 같이 Memcached가 먼저 개발되고 Redis가 나중에 개발 되었습니다. 이것을 보면 Memcached의 성능을 보완해서 나온것이 Redis라는 것을 유추할 수 있고 실제로도 그렇다고 합니다.



**Memcached와 Redis는 모두 *NoSQL* 데이터 관리 솔루션 제품군**에 속하며 둘 다 “**key-value**” 데이터 모델을 기반으로합니다. 또한, Memcached 와 Redis 는 인메모리 위에서 동작하는 “key-value” 스토리지이며 둘다 인기 있는 완성된 오픈 소프 프로젝트입니다. **둘 다 모든 데이터를 RAM에 보관하므로 캐싱 레이어로 매우 유용합니다.** 성능 측면에서도 두 데이터 저장소는 매우 유사하여 처리량 및 지연 시간과 관련하여 거의 동일한 특성을 나타냅니다.

***NoSQL : 특정 데이터베이스를 지칭하는 것이 아니라 빅데이터를 처리하기 위한 데이터저장소를 통칭한다***







#### 참고

- [Why Redis beats Memcached for caching](https://www.infoworld.com/article/3063161/why-redis-beats-memcached-for-caching.html)

- [[NoSQL & Cache] Redis vs Memcached ( 왜 Redis 를 사용해야 하는가? )](http://blog.leekyoungil.com/?p=200)

- [System Properties Comparison Ehcache vs. Memcached vs. Redis](https://db-engines.com/en/system/Ehcache%3bMemcached%3bRedis)
- [DB-Engines Ranking - Trend of Ehcache vs. Memcached vs. Redis Popularity]()
- [DB-Engines Ranking](https://db-engines.com/en/ranking)

- [DevOps 엔지니어의 Redis Test 분투기 - Part 1](https://helloworld.kurly.com/blog/redis-fight-part-1/)
- [이것이 레디스다 초고속 읽기 쓰기를 제공하는 인메모리 기반 NoSQL, Redis](https://book.naver.com/bookdb/book_detail.nhn?bid=7334741)

- **[about memcached](http://www.memcached.org/about)**