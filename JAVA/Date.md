# Date



**Java 시간 API 시대 흐름순**

java.util.Date > java.util.Calendar > java.time(org.joda.time)



### LocalDate

**개념**

------

로컬 날짜 클래스로 **날짜 정보만** 필요할 때 사용

**날짜 정보**만 출력됩니다 **날짜 정보**만



**문법**

------

```
// 로컬 컴퓨터의 현재 날짜 정보를 저장한 LocalDate 객체를 리턴
LocalDate currentDate = LocalDate.now();
// result : 2019-11-13

// 파라미터로 주어진 날짜 정보를 저장한 LocalDate 객체를 리턴한다.
LocalDate targetDate = LocalDate.of(2019,11,12);
 //결과 : 2019-11-12
```

 



### LocalTime

**개념**

------

로컬 시간 클래스로 **시간 정보**만 필요할 때 사용

**시간 정보**만 출력됩니다 **시간 정보**만

 

**문법**

------

```
// 로컬 컴퓨터의 현재 시간 정보를 저장한 LocalDate 객체를 리턴. 
LocalTime currentTime = LocalTime.now();   
// 결과 : 18:34:22

// 파라미터로 주어진 시간 정보를 저장한 LocalTime 객체를 리턴.
LocalTime targetTime = LocalTime.of(12,33,35,22); 
// 끝에 4번째 매개변수는 nanoSecond 인데 선택 값이다 굳이 쓰지 않아도 된다.
// 결과 : 12:32:33.0000022
```

 

### **LocalDateTime**

**개념**

------

**날짜와 시간 정보** 모두가 필요할 때 사용**.**

**날짜와 시간 정보 출력**

 

**문법**

------

```
// 로컬 컴퓨터의 현재 날짜와 시간 정보
LocalDateTime currentDateTime = LocalDateTime.now();    
// 결과 : 2019-11-12T16:34:30.388

LocalDateTime targetDateTime = LocalDateTime.of(2019, 11, 12, 12, 32,22,3333);
// 여기도 second,nanoSecond 매개변수는 필수가 아닌 선택입니다.
// 결과 : 2019-11-12T12:32:22.000003333
```



**날짜 더하기**

```
LocalDateTime currentDateTime = LocalDateTime.now();
// 더 하기는 plus***() 빼기는 minus***()
// currentDateTime.plusYears(long) or minusYears(long)
currentDateTime.plusDays(2)
// 결과 : 2019-11-14T12:32:22.000003333
```

| 리턴 타입               | 메소드(매개변수) | 설명   |
| ----------------------- | ---------------- | ------ |
| java.time.LocalDateTime | plusYears()      | 년     |
| java.time.LocalDateTime | plusMonths()     | 월     |
| java.time.LocalDateTime | plusWeeks()      | 주     |
| java.time.LocalDateTime | plusDays()       | 일     |
| java.time.LocalDateTime | plusHours()      | 시     |
| java.time.LocalDateTime | plusMinutes()    | 분     |
| java.time.LocalDateTime | plusSeconds()    | 초     |
| java.time.LocalDateTime | plusNanos()      | 밀리초 |

**빼기도 동일 minusYear(),minusMonths() …**



**날짜 비교**

```
LocalDateTime startDateTime = LocalDateTime.now();  
// 결과 : 2019-11-12T12:32:22.000003332
LocalDateTime endDateTime = LocalDateTime.of(2019, 11, 12,12, 32,22,3333);
// 결과 : 2019-11-12T12:32:22.000003333

// startDateTime이 endDateTime 보다 이전 날짜 인지 비교
startDateTime.isBefore(endDateTime);    
// 결과 : true

// 동일 날짜인지 비교
startDateTime.isEqual(endDateTime);
// 결과 : false

// startDateTime이 endDateTime 보다 이후 날짜인지 비교
startDateTime.isAfter(endDateTime); 
// 결과 : false
```

**주의 : nano 초가 존재할 경우 나노초 시간까지 비교**

**날짜 차이 계산**

```
LocalDate startDate = LocalDate.now(); 
// 결과 : 2019-11-12
LocalDate endDate = LocalDate.of(2019,12,13);
// 결과 : 2019-12-13

Period period = Period.between(startDate, endDate);

period.getYears();      // 0년
period.getMonths();     // 1개월
period.getDays();       // 1일 차이
```

**주의 : startDate와 end가 31일 차이가 나서 리턴이 31일이 되는 것이 아니라 1개월 1일로 반환됩니다.**

**무심코 period.getDays()로 비교했다간 다칠 수 있습니다.**

 

**그렇다면 31일을 반환 하려면?**

 

**전체 시간을 기준으로 차이 계산하기**

```
LocalDate startDate = LocalDate.now(); 
// 결과 : 2019-11-12
LocalDate endDate = LocalDate.of(2019,12,13);
// 결과 : 2019-12-13

ChronoUnit.DAYS.between(startDate, endDate); 
// 결과 : 31 (1개월 1일)
```

| 클래스             | 설명             |
| ------------------ | ---------------- |
| ChronoUnit.YEARS   | 전체 년 차이     |
| ChronoUnit.MONTHS  | 전체 월 차이     |
| ChronoUnit.WEEKS   | 전체 주 차이     |
| ChronoUnit.DAYS    | 전체 일 차이     |
| ChronoUnit.HOURS   | 전체 시간 차이   |
| ChronoUnit.SECONDS | 전체 초 차이     |
| ChronoUnit.MILLIS  | 전체 밀리초 차이 |
| ChronoUnit.NANOS   | 전체 나노초 차이 |

 

**시간 차이 계산**

```
LocalTime startTime = LocalTime.now();  
// 결과 : 17:14:55
LocalTime endTime = LocalTime.of(18,17,35);
// 결과 : 18:17:35

Duration duration = Duration.between(startTime, endTime);
duration.getSeconds();      
// 결과 : 3742
duration.getNano();
// 결과 : 922000000
```

 

**날짜 포맷**

```
LocalDateTime now = LocalDateTime.now();
DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy년 M월 d일 a h시 m분");
String nowString = now.format(dateTimeFormatter);   
// 결과 : 2019년 11월 12일 오후 7시 2분

LocalDateTime now2 = LocalDateTime.now();  
DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss");
// 결과 : 2019-11-12 07:26:12
```

**주의 : 포맷의 두번째 예제에 07는 19시입니다. 24시간 표기가 아닙니다.** 

------

**날짜 변환**

 

**LocalDate -> String**

```
LocalDate.of(2020, 12, 12).format(DateTimeFormatter.BASIC_ISO_DATE);
```

**LocalDateTime -> String**

```
LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
```

**LocalDate -> java.sql.Date**

```
Date.valueOf(LocalDate.of(2019, 12, 27));
```

**LocalDateTime -> java.util.Date**

```
Date.from(LocalDateTime.now().atZone(ZoneId.systemDefault()).toInstant());
```

**LocalDateTime -> java.sql.Timestamp**

```
Timestamp.valueOf(LocalDateTime.now());
```

**String -> LocalDate**

```
LocalDate.parse("1995-05-09");
LocalDate.parse("20191224", DateTimeFormatter.BASIC_ISO_DATE); 
```

**String -> LocalDateTime**

```
LocalDateTime.parse("2019-12-25T10:15:30");
LocalDateTime.parse("2019-12-25 12:30:00", DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
```

**java.util.Date -> LocalDateTime**

```
LocalDateTime.ofInstant(new Date().toInstant(), ZoneId.systemDefault());
```

**LocalDateTime -> LocalDate**

```
LocalDate.from(LocalDateTime.now());
```

**LocalDate -> LocalDateTime**

```
LocalDate.now().atTime(2, 30);
```

 

날짜 변환 [jekalmin의 블로그] 참조

 

 

**해당 월에 마지막 날짜 찾기**

```
String targetDate = "2020-02-02";

YearMonth targetYearMonth = YearMonth.from(LocalDate.parse(targetDate, DateTimeFormatter.ofPattern("yyyy-MM-dd")));

//해당 월의 일 수(int)
System.out.println(targetYearMonth.lengthOfMonth()); // 29

//해당 월의 마지막 날(LocalDate)
System.out.println(targetYearMonth.atEndOfMonth()); // 2020-02-29
```

**해당 주차의 날짜 찾기**

```
final long calendarWeek = 34; //34주차 입력
LocalDate desiredDate = LocalDate.now()
            .with(IsoFields.WEEK_OF_WEEK_BASED_YEAR, calendarWeek)
            .with(TemporalAdjusters.previousOrSame(DayOfWeek.MONDAY));
//결과 : 2020-08-17 
//DayOfWeek.MONDAY = 해당 주차에 월요일
```

 

**TMI((Too Much Information)**

------

위에 예제처럼 LocalDateTime startDateTime = LocalDateTime.now()[;](https://java119.tistory.com/manage/newpost/LocalDateTime.now();) 하게 되면

결과 : 2019-11-12T12:32:22.000003332 이러한 결과가 나오는데 여기서 중간에 T는 뭘까?

바로 **ISO** 형식 시간표기법이다.

 

그 말은 즉, String으로 날라온 매개변수를 LocalDateTime로 파싱할때

'T'가 없으면 java.time.format.DateTimeParseException이 발생한다는 뜻입니다.

 

**반짝 예시**

```
String date = "2019-11-12 12:30:54"
LocalDateTime localdatetime = LocalDateTime.parse(date);
// 결과 : java.time.format.DateTimeParseException

String date = "2019-11-12T 12:30:54";
LocalDateTime localdatetime = LocalDateTime.parse(date);
// 결과 : parse 성공
```

 

#### copy

- https://java119.tistory.com/52



#### 참조

- https://java119.tistory.com/24
- https://namocom.tistory.com/673
- [Java - 자바 날짜&시간 java.time 패키지(LocalDateTime, ZoneDateTime)](https://coding-start.tistory.com/373) -나라마다 시간을 어떻게 맞추는가? -> ***ISO-8601***
- [java.util.Date 쓰다 삽질한 내용…](https://blusky10.tistory.com/380)

- [Java의 날짜와 시간 API](https://d2.naver.com/helloworld/645609) - naver d2

- [JAVA에서 날짜,시간 제대로 사용하는 LocalDate, LocalTime, LocalDateTime (NTP 시간 서버에서 정확한 시간 받아오기, json object 받기, JPA 테스트 with LocalDateTime)](https://jeong-pro.tistory.com/163)

  