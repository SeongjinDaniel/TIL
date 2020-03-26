# R 함수 정리

#### sum(), min(), max(), mean()

```R
x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum(x);min(x);max(x);mean(x);
```

#### stop()

```R
stop("~~~") # 에러를 발생시키는 함수
```

#### warning()

```R
warning("~~~") # warning을 발생시키는 함수
```

#### rep()

```R
rep(1, 100) # 100번 반복해서 1을 대입
rep(1:3, 5) # 1, 2, 3을 5번 반복 아규먼트가 없으면 기본으로 times가 받아서 사용된다.
rep(1:3, times=5) # 위와 결과 같음 times는 아규먼트, 전달하고자 하는 값 앞에 다가 매개변수 이름을 정의 할수있다.
                  # 이것을 키워드 파라미터 라고 한다.
rep(1:3, each=5) # each는 1, 2, 3 각각 5번씩 반복
```

#### print()

```R
print() # 출력
```

#### length()

```R
length(LETTERS) # 26 출력
length(month.name) # 12 출력
length(pi) # 1 출력
```

#### class()

```R
x <- c(10,2,7,4,15)
class(x) # numeric 출력
```

#### rev()

```R
x <- c(10,2,7,4,15)
rev(x) # 거꾸로 출력
```

#### range()

```R
x <- c(10,2,7,4,15)
range(x) # 최솟값 최댓값
```

#### sort()

```R
x <- c(10,2,7,4,15)
sort(x) # 작은 값에서 큰 값 순으로
sort(x, decreasing = TRUE) # 큰 값에서 작은값으로로
sort(x, decreasing = T)
x <- sort(x) # sort하고 대입 작은것 
```

#### order()

```R
x <- c(10,2,7,4,15)
order(x) # 작은 순서대로 index를 알려준다.
```

#### names()

```R
x <- c(10,2,7,4,15)
# 원소마다 이름이 부여된 벡터
names(x) # Getter로 사용된다. name 벡터가 없어서 NULL이 출력된다.
names(x) <- LETTERS[1:5] # x는 name 벡터가 됐다.
names(x) <- NULL
x[2];x["B"] # 인덱스로 숫자 대신에 문자열 형식으로 설정해서 출력 할 수 있다.
x[B] # 여기서 B는 변수명
x[B()] # 여기서 B()는 함수
```

#### ls()

```R
ls() # 지금까지 만들어진 객체들의 List를 보여준다.
```

#### rm()

```R
rm(x) # 객체 삭제
```

#### which()

```R
which(rainfall > 100) # TRUE인 것에 Index가 나온다. 몇월인지 궁금할 때 사용된다.
month.name[which(rainfall > 100)]
month.abb[which(rainfall > 100)]
month.korname <- c("1월","2월","3월",
                   "4월","5월","6월",
                   "7월","8월","9월",
                   "10월","11월","12월")
month.korname[which(rainfall > 100)]
which.max(rainfall)
which.min(rainfall)
month.korname[which.max(rainfall)]
month.korname[which.min(rainfall)]

month.korname <- c("일요일", "월요일", "화요일",
                   "수요일", "목요일", 
                   "금요일", "토요일")

paste(month.korname, count, sep = ":") # paste 함수 :원소별로 문자열 결합, sep의 default는 공백이다. 
                                       # 그냥 붙이고 싶으면 "" 널값 사용
month.korname[which.max(count)]
month.korname[which.min(count)]
month.korname[which(count > 50)]
```

#### sample()

```R
sample(1:20, 3) # 1 ~ 20 까지 3개 꺼냄
sample(1:45, 6) # 1 ~ 45까지 중복을 제거하여 6개 꺼냄
sample(1:10, 7) # 1 ~ 10까지 중복을 제거하여 7개 꺼냄
sample(1:10, 7, replace=T) # replace=T: 중복 허용

count <- sample(1:100,7)
```

#### paste()

```R
paste(month.korname, count, sep = ":") # paste 함수 :원소별로 문자열 결합, sep의 default는 공백이다. 
                                       # 그냥 붙이고 싶으면 "" 널값 사용

paste("I'm","Duli","!!") # 몇개가 오든 상관없다. delimeter : 데이터 분리 기호
paste("I'm","Duli","!!", sep="")
paste0("I'm","Duli","!!") # paster함수는 기본적으로 paste와 paste0는 사용하는 delimeter가 뭐냐의 차이이다.

fruit <- c("Apple", "Banana", "Strawberry")
food <- c("Pie","Juice", "Cake")

?paste
paste(fruit, food, sep="")
paste(fruit, food, sep=":::")
paste(fruit, food, sep="", collapse="-") # collapse를 주지 않으면 기본값은 NULL이다
                                         # 각각 결합한것을 가지고 3개의 문자를 하나의 문자열로 변경
paste(fruit, food, sep="", collapse="")
paste(fruit, food, collapse=",")
```

#### matrix()

```R
x1 <- matrix(1:8, nrow = 2)
x1
x1<-x1*3
x1

sum(x1); min(x1);max(x1);mean(x1)

x2 <-matrix(1:8, nrow =3)
x2

(chars <- letters[1:10]) # 괄호치면 출력만 하고 없으면 저장도 한다.

mat1 <-matrix(chars) # matrix에 행열을 주지 않았기 때문에 10행 1열(열을 우선적으로 체운다.)
mat1; dim(mat1) # dim: 행 열
matrix(chars, nrow=1)
matrix(chars, nrow=5)
matrix(chars, nrow=5, byrow=T) # 행우선
matrix(chars, ncol=5)
matrix(chars, ncol=5, byrow=T)
matrix(chars, nrow=3, ncol=5)
matrix(chars, nrow=3)
```

#### rbind(), cbind()

```R
vec1 <- c(1,2,3)
vec2 <- c(4,5,6)
vec3 <- c(7,8,9)
mat1 <- rbind(vec1,vec2,vec3); mat1 # 행 단위로 붙임, 행의 이름이 나옴
mat2 <- cbind(vec1,vec2,vec3); mat2 # 열 단위로 붙임, 열의 이름이 나옴
```

#### 결과

```
     [,1] [,2] [,3]
vec1    1    2    3
vec2    4    5    6
vec3    7    8    9

     vec1 vec2 vec3
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

