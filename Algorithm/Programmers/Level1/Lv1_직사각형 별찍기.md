# Lv1_직사각형 별찍기



#### Question

- [Lv1_직사각형 별찍기](https://programmers.co.kr/learn/courses/30/lessons/12969)



#### Mine

```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        for(int i = 0; i < b; i++) {
            for(int j = 0; j < a; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
```



#### Others

```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<a; i++){
            sb.append("*");
        }
        for(int i=0; i<b; i++){
            System.out.println(sb.toString());
        }
    }
}
```

