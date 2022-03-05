# Dart URL 코드



```dart
import 'package:http/http.dart' as http;

void main() async {
  // URL : https://www.googleapis.com/books/v1/volumes?q=고양이
  final url = Uri.https('www.googleapis.com', '/books/v1/volumes', {'q': '고양이'});

  // GET 방식 요청
  final res = await http.get(url);

  if (res.statusCode == 200) {
    // 성공시
    print(res.body);
  } else {
    // 실패시
    print(res.statusCode);
  }
}
```

![image](https://user-images.githubusercontent.com/55625864/156870206-be191bab-4d08-487e-b653-ee3e12cafae9.png)
