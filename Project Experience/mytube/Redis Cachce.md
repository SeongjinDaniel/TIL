# 레디스 캐시



레디스로 캐시하려면 우선 레디스에게 캐싱을 위임하는 RedisCacheManager를 구성한다. RedisCacheManager는 실제 작업을 RedisTemplate에 떠넘긴다.