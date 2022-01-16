# Python Install Library

- bs4 (beautifulsoup4)
  
  - 크롤링 사용

- pymongo

- MongoDB 사용

- certifi
  MogoClient 오류 났을 때 사용
  
  - 인증 관련
  
  **참고**
  
  ```python
  from pymongo import MongoClient
  import certifi
  
  ca = certifi.where()
  client = MongoClient('mongodb+srv://test:sparta@cluster0.ykr9q.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
  db = client.dbsparta
  ```

- dnspython

- Flask
  
  - > 플라스크는 파이썬으로 작성된 마이크로 웹 프레임워크의 하나로, Werkzeug 툴킷과 Jinja2 템플릿 엔진에 기반을 둔다. (구글 위키백과)