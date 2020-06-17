# Null Function

☘️표시는 안했지만 scott 계정에서 EMP데이터를 가져오는 것이 아니라면 반드시 ***FROM DUAL*** 써줘야 합니다! 



#### * NVL

##### NULL인 데이터는 0으로 환산하게 하는 함수

~~~sql
NVL (NULL인지 여부를 검사할 데이터 또는 열, 앞의 데이터가 NULL일 경우 반환할 데이터)

SELECT NVL(COMM, 0)
FROM EMP
~~~



#### *NVL2

##### NULL이 아닐 때 반환할 데이터를 추가로 지정해줄 수 있다. 

~~~SQL
NVL2 (NULL인지 여부를 검사할 데이터 또는 열, 앞 데이터가 NULL이 아닐 경우 반환할 데이터 또는 계산식, 
     앞 데이터가  NULL일 경우 반환할 데이터 또는 계산식)

FOR EXAMPLE!
COMM 열이 NULL이 아니라면 O를 , NULL 이라면 x를 표시하여 확인할 수 있다. 
--below functin은 위 글의 example이다.
SELECT NVL2(COMM, '0', 'X')
~~~


