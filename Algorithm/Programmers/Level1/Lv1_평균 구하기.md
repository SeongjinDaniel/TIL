# Lv1_평균 구하기



#### Question

- [평균구하기](https://programmers.co.kr/learn/courses/30/lessons/12944)



#### Mine

```java
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double sum = 0;
        for(int data : arr) {
            sum += data;
        }
        answer = sum / arr.length;
        return answer;
    }
}
```



#### Second Mine

```java
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int len = arr.length;
        for (int i = 0; i < len; i++) {
            answer += arr[i];
        }
        answer /= len;
        return answer;
    }
}
```



#### Others

```java
import java.util.Arrays;

public class GetMean {
    public int getMean(int[] array) {
        return (int) Arrays.stream(array).average().orElse(0);
    }

    public static void main(String[] args) {
        int x[] = {5, 4, 3};
        GetMean getMean = new GetMean();
        // 아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("평균값 : " + getMean.getMean(x));
    }
}
```

average()는 평균을 구하는 메소드고, orElse(double other)은 average의 값이 있으면 average를 리턴하고 값이 없으면other을 리턴하는 메소드라고 하네요