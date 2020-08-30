# Lv1_하샤드 수



#### Question

- [Lv1_하샤드 수](https://programmers.co.kr/learn/courses/30/lessons/12947#)



#### Mine

```java
class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String s = String.valueOf(x);
        int sum = 0;

        for(int i = 0; i < s.length(); i++) {
            sum += s.charAt(i) - '0';
        }

        if(x % sum != 0) {
            answer = false;
        }

        return answer;
    }
}
```



#### Others

```java
public class HarshadNumber{
    public boolean isHarshad(int num){

    String[] temp = String.valueOf(num).split("");

    int sum = 0;
    for (String s : temp) {
        sum += Integer.parseInt(s);
    }

    if (num % sum == 0) {
            return true;
    } else {
      return false;
    }
    }

       // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        HarshadNumber sn = new HarshadNumber();
        System.out.println(sn.isHarshad(18));
    }
}
```



#### Others

```java
import java.util.function.IntConsumer;

public class HarshadNumber{
    private int sum = 0;
    public boolean isHarshad(int num){
        sum = 0;
        Integer.toString(num).chars().forEach(c -> sum += c - '0');
        return num % sum == 0;
    }

       // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        HarshadNumber sn = new HarshadNumber();
        System.out.println(sn.isHarshad(18));
    }
}
```



#### Others

```java
public class HarshadNumber{
    public boolean isHarshad(int num){
int mod=num;
int calc=0;
do{
 calc+=(mod%10);
mod=mod/10;
}while(mod%10 > 0);

        return (num%calc == 0) ? true:false;//or fralse
    }
}
```

