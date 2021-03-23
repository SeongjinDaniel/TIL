# Web Storage API

## 웹 스토리지란?

- 웹 브라우저에 자료를 저장하기 위한 기능으로 로컬스토리지와 세션스토리지로 나뉜다.

- 기존의 쿠키와 비슷핚 기술이지만 일부 기능에서 차이를 가지고 있다.

- 저장하려는 데이터릴다 유일한 이름(키)을 같이 저장핚다.

- 저장하려는 데이터의 종류에는 제핚이 없으며 저장시에는 문자열로 저장된다

- 로컬스토리지(local storage) : 영구 보관

- 세션스토리지(session storage) : 브라우저가 종료될 때까지 보관

- W3C는 Same Origin Policy에 따라 도메읶당 5MB를 권장하고 있으며 추가 용량이 픿요핛 경우 사용자의 동의를 얻어 용량을 확장할 수 있다.(초과시 QUOTA_EXCEEDED-ERR 발생)
  
  ps) Same Origin Policy를 사용하고 있으면 웹 페이지가 달라도 공유가 가능하다(어떻게 ? Javascript를 가지고있는 HTML을 통해서
  
- Same Orign Policy 정책이 적용된다.

----------

#### window.localStorage 와 window.sessionStorage 의 주요 멤버

- length : 스토리지에 저장된 key/value 쌍의 개수를 추출하는 속성이다.

- key(index) : 숫자형 인덱스에 해당하는 key를 리턴한다.

- getItem(key) : 스토리지로 부터 key 에 해당하는 value 를 추출한다.

- setItem(key, value) : 스토리지에 key 에 해당하는 value 를 저장한다.

- removeItem(string key) : 스토리지에 key 에 해당하는 value 를 제거한다.

- clear() : 현재 스토리지의 모든 데이터를 제거한다.

- onstorage : 로컬 스토리지의 내용이 벾경될 때릴다 발생되는 이벤트로 로컬 스토리지의

  변경 사항을 모니터릳 하는 것이 가능하다. StorageEvent 객체가 생성된다.

  (ps, on이라는 것에서 Event형이라는것을 알 수 있다.)

  [ StorageEvent 객체의 주요 속성 ]
  –key : 추가, 삭제, 변경된 키 이름
  –oldValue : 업데이트되기 전의 값으로 새로 추가된 값이면 null
  –newValue : 새로 업데이트된 값으로 기존 값을 삭제할 경우에는 null
  –url : 변경사항이 발생된 페이지의 URL

#### 로컬 스토리지의 데이터 관리

- 저장
  localStorage.mykey = "myvalue";
  localStorage["mykey"] = "myvalue";
  localStorage.setItem("mykey", "myvalue");
- 읽기
  var mydata = localStorage.mykey;
  var mydata = localStorage["mykey"];
  var mydata = localStorage.getItem("mykey”);
- 삭제
  delete localStorage.mykey;
  delete localStorage["mykey"];
  localStorage.removeItem("mykey");



XML, CSV, JSON 순으로 많이 사용한다.

https://www.json.org/json-en.html -> 즐겨찾기 추가 필수!

-> canvas_memo.html , canvas_memo.js 다시 확인!!  저장 기능 확인! 