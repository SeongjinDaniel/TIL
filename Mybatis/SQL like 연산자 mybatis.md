# SQL like 연산자 mybatis



#### <LIKE연산자>


조건식 구성 : 컬럼명  LIKE 'pattern'

※패턴의 횟수를 표현하는 예약문자(와일드카드)
 % : 0~무한대의 문자를 대체
 _ : 단 1개의 문자를 대체

----> 와일드카드 없이 비교했을때는 컬럼명 = '데이터' 와 다르지 않다!!
   예)  ename='MARTIN'
     ename like 'MARTIN'

  'M%' ---> M으로 시작되는 문자들
  '%M' ---> M으로 끝나는 문자들
  'M_ _ _A' ----> 전체 문자길이가 5이고 첫글자 'M' 마지막글자 'A'로 끝나는 문자들.



#### 참조

- [sql like 연산자 mybatis사용](https://dodong2.tistory.com/4)