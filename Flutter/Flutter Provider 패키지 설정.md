# Flutter Provider 패키지 설정


:bulb: **Provider**를 이용하여 **BucketService**를 위젯 트리(Widget tree)의 꼭대기에 배치하고, 어디서든 쉽게 접근할 수 있도록 만들어 줍니다.

1. 코드스니펫을 복사해 `main.dart` 파일에 6번째 라인을 변경해주세요.
   
   - **[코드스니펫] Provider init**
     
     ```dart
     MultiProvider(
          providers: [
            ChangeNotifierProvider(create: (context) => BucketService()),
          ],
          child: const MyApp(),
        ),
     ```

  :bulb: `MultiProvider`로 `MyApp`을 감싸서 모든 위젯들의 최상단에 `provider`들을 등록해줍니다. `MultiProvider`는 위젯트리 꼭대기에 여러 서비스들을 등록할 수 있도록 만들 때 사용합니다.

💡 **BucketService**는 `bucketList` 값이 변하는 경우 `HomePage`에 변경사항을 알려주도록 구현해야 하므로 `ChangeNotifierProvider`로 **Provider**에 등록해줍니다.  

![image](https://user-images.githubusercontent.com/55625864/153719770-32785553-b7ea-4b07-8466-a5e1587fa265.png)

2. **Provider**와 **BucketService**가 `Import` 되지 않아 에러가 발생합니다.
   
   6번째 라인에 `MultiProvider`를 클릭한 뒤 Quick Fix(`Ctrl/Cmd + .`)를 눌르고 `Import 'package:provider/provider.dart';`를 선택해주세요.
   
   
   :bulb: 만약 `import 'package:provider/provider.dart';`가 안보이신다면 `pubspec.yaml` 파일을 열고 저장 단축키를 눌러주세요.
   
   저장 단축키
   window : `Ctrl + S` macOS : `Cmd + S`
   
   ![image](https://user-images.githubusercontent.com/55625864/153719923-174a727f-1584-4316-ab34-53bc818b5ad6.png)

3. 마찬가지로 9번째 라인 **BucketService**를 클릭하신 뒤 `import 'bucket_service.dart';`를 선택해주세요.
   
   ![image](https://user-images.githubusercontent.com/55625864/153720018-c6e2caa1-7768-4a16-8be0-6a7dbef8a020.png)
   
   **Provider** 설정이 완료 되었습니다.
   
   ![image](https://user-images.githubusercontent.com/55625864/153720027-5e5296fb-9f13-4068-ae33-c4636376915a.png)

4. `Restart`를 클릭해주세요.
   
   <img src="https://user-images.githubusercontent.com/55625864/153720028-44451b58-a682-4657-a3d0-2de59c65668c.png" title="" alt="image" width="331">
