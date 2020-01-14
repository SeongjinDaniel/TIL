# Drag & Drop

### Drag&Drop 이란?

- Drag&Drop 은 사용자 편의성을 고려한 UI 기능이다.
- 마우스를 사용하여 애플리케이션 갂에 파일이나 애플리케이션의 데이터를 전달하는 기능으로서 다양한 이벤트의 핸들러를 구현하여 처리한다.
- 웹 애플리케이션에서는 화면 상에 나타나는 요소를 옮기거나 외부에 있는 파일을 인어 웹 페이지에 출력 또는 업로드 하는 용도로 사용된다.
- HTML5 의 엘리먼트들은 draggable 속성의 값을 true 로 지정하면 드래그가 가능한 소스객체가 된다.
- \<img> 엘리먼트는 디폴트로 draggable 속성의 값이 true 이며 다른 엘리먼트들은 설정해주어야 한다.

- 드래그가 가능한 대상(소스 객체)
  - dragstart 이벤트(필수)
  - dragend 이벤트
  - drag 이벤트
- 드롭이 가능한 영역(타겟 객체)
  - dragenter 이벤트
  - dragleave 이벤트
  - dragover 이벤트
  - drop 이벤트

### 드래그 앤 드롭 이벤트

- dragstart 이벤트
  •엘리먼트에서 드래그를 시작할 때 발생
- drag 이벤트
  •드래그하는 동앆 일어나는 연속적인 이벤트
  •마우스 커서를 움직일 때 드래그 이벤트가 드래그 소스에서 반복적으로 호출된다.
  •drag 이벤트가 일어나는 동안 나타나는 드래그 피드백의 형태는 바꿀 수 있지만 dataTransfer에 있는 데이터에는 접근할 수 없다.
- dragenter 이벤트
  •드래그된 요소가 드롭 동작을 수행하기 위해 dropzone 영역에 들어 갔을 때 발생하는 이벤트
- dragleave 이벤트
  •드래그된 엘리먼트를 드롭 동작을 하지 않고 dropzone 영역을 벖어날 때 발생하는 이벤트
- dragover 이벤트
  •드래그된 엘리먼트가 dropzone 영역에서 움직일 때 발생하는 이벤트
  •드래그 소스에서 호출되는 drag 이벤트와는 달리 이 이벤트는 마우스의 현재 타깃에서 호출된다.
- drop 이벤트
  •사용자가 릴우스 버튼을 놓을 때 현재 마우스 타깃에서 호출
- dragend 이벤트
  •연쇄 작용의 마지막 단계에서 일어나는 이벤트로 drop 이벤트 후 발생한다.
  •드래그 소스에서 발생하여 드래그가 완료되었다는 것을 나타낸다.

### dataTransfer 객체

- 드래그되는 소스객체에서 드롡이 읷어나는 타겟 객체로 젂달하려는 데이터를 저장하는 객체이다.
- dragstart 이벤트 발생시 젂달되는 이벤트 객체의 dataTransfer 속성을 사용핚다.
- dataTransfer 객체의 주요 속성과 메서드
  - files 속성 : FileList 타입으로, 드래그 대상이 파일일 때 사용된다.
  - types 속성 : StringList 타입으로, 젂달되는 데이터들의 타입명을 추출할 수 있다.
  - clearData(type) : type 명에 해당되는 데이터를 삭제한다.
  - getData(type) : type 명에 해당되는 데이터를 추출한다.
  - setData(type, data) : type 명으로 데이터를 저장한다.
  - setDragImage(image, x, y) : 드래그하는 동안 커서를 따라다니는 이미지를 (x,y)
    위치에 출력되도록 설정한다.

### 파일에 대한 Drag & Drop

"drop" evt → (var dt = evt.dataTransfer;) → DataTransfer → (var files = dt.files;) → files → (files[i]) → FileReader readAsDataURL(files[i]) → (FileReader.onload Handler) → "load" evt → (var dataURL = evt.target.result;) → dataURL → (imageElem.src = dataURL;) → Image!!! 

## File API

### HTML5 File API의 특징
- HTML5에서는 로컬 컴퓨터에 있는 파일을 웹 애플리케이션이 읽을 수 있는 기능을 제공한다.
- 텍스트 형식 뿐만 아니라 이진(binary)형식도 읽는 것이 가능하다.
- 읽는 기능 뿐만 아니라 출력과 생성기능도 스펙이 제안되기도 했지만 현재로서는 인는 기능의 스펙만 남고 출력이나 생성 기능의 API는 제거되었다.
- File API
  - 파일에 대한 정보를 알아내기 위핚 기능을 지원하는 **File** 객체
  - 파일의 내용을 읽어들이는 기능을 지원하는 **FileReader** 객체

### File 객체

- 로컬하드디스크에 존재하는 파읷의 정보를 추출하거나 조작할 수 있는 멤버를 제공한다.
- name : 파일의 이름을 추출하는 기능의 속성이다.
- type : 파일의 MIME Type (알 수 없을 때는 null)정보를 추출하는 기능의 속성이다.
- size : 파일의 크기를 추출하는 기능의 속성이다.
- lastModifiedDate : 파일의 마지막 수정일을 추출하는 기능의 속성이다.
- slice(start, length, contentType) : 파일에서 시작위치(start)부터 length만큼 파일의 내용을 Blob 객체로 리턴한다.

### FileReader 객체

- 로컬하드디스크에 존재하는 파일의 내용을 인는 기능을 제공한다.
- readAsText(Blob 또는 File 객체, encoding) : 파일 내용을 텍스트 문자열로 읽는다.
  두 번째 인자로는 파일의 문자 인코딩을 지정한다.(생략 시는 UTF-8)
- readAsDataURL(Blob 또는 File 객체) : 파일 내용을 data: 으로 시작하는 DataURL 형식의 문자열로 읽는다.
- readAsBinaryString(Blob 또는 File 객체) : 파일의 내용을 바이너리 형식으로 읽는다.
- readAsArrayBuffer(Blob 또는 File 객체) : 파일의 내용을 읽어서 ArrayBuffer 객체에 저장한다.
- abort() : 읽는 작업을 중간에 중지한다.
- result : 읽어들인 파일의 내용 추출하는 용도로 사용되는 속성이다.
- error : 에러 발생 시의 에러 정보를 추출하는 용도로 사용되는 속성이다.

FileList
File 객체들을 담고 있는 배열과 같은 객체이다.
파읷에 대핚 드래그 앤 드롡에서 dataTransfer 객체를 통해 또는
<input type="file"> 태그의 DOM 객체를 통해서 사용되는 files 속성의 타입이다.
length : 저장된 File 객체들의 크기를 추출핛 수 있는 속성이다.
item(index) : index 위치의 File 객체를 추출하는 기능의 메서드이다.

### Blob

- 실제 데이터들을 표현하는 객체이다.
- type : 파읷의 MIME Type (알 수 없을 때는 null)정보를 추출하는 기능의 속성이다.
- size : 파읷의 크기를 추출하는 기능의 속성이다.
- slice(start, length, contentType) : 파읷에서 시작위치(start)부터 length릶큼 파읷의 내용을 Blob 객체로 리턴핚다.