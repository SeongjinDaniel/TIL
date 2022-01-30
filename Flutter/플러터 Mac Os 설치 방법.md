# 플러터 Mac Os 설치 방법



- **MacOS 프로그램 설치 방법**
  
  - 1. **Flutter**
    - 다운로드
      
      1. Chrome 브라우저에서 [링크](https://docs.flutter.dev/get-started/install/macos)를 열어주세요.
      
      2. 밑으로 조금 스크롤한 뒤, 파란색 버튼을 클릭해
         
         ![image](https://user-images.githubusercontent.com/55625864/151692958-05bd3259-d7e4-4f23-90d6-c0b20a8a71ed.png)
      
      3. 다운로드를 진행해 주세요.
         
         <aside>
         💡 위치를 변경하지 말고, 꼭 `다운로드` 폴더에 그대로 진행해 주세요!
         
         </aside>
         
         <img src="https://user-images.githubusercontent.com/55625864/151693102-b0c98874-3844-4d0d-b6a5-1a33429773dd.png" title="" alt="image" width="397">
      
      4. 바탕화면에서 휴지통 우측에 있는 `다운로드` 폴더를 선택한 뒤 `Finder에서 열기` 버튼을 눌러 주세요.
         
         <img src="https://user-images.githubusercontent.com/55625864/151693160-1ed97b35-e5fa-40a9-9f32-bd2c60b0d0c1.png" title="" alt="image" width="459">
      
      5. 다운받은 flutter 압축 파일을 실행해 주세요.
         
         ![image](https://user-images.githubusercontent.com/55625864/151693213-f3db652d-4c92-4661-8871-31e733b1ccee.png)
      
      6. 아래 사진과 같이 압축이 해제되고 `flutter`라는 폴더가 생성 됩니다.
         
         <aside>
         💡 만약 압축이 해제된 폴더 이름이 아래 사진과 다른 경우 `flutter`로 변경해 주시기 바랍니다.
         
         </aside>
         
         <img src="file:///Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-17-56-51-image.png" title="" alt="" width="485">
    
    - 환경변수 설정 및 설치
      
      1. macOS 우측 상단에 `돋보기 🔍` 아이콘을 선택해 주세요. 그러면 아래와 같이 `Spotlight 검색` 창이 뜹니다.
         
         ![](/Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-17-56-35-image.png)
      
      2. `Spotlight`에 `terminal`이라고 검색한 뒤, 아래와 같이 하단에 `터미널` 프로그램이 보이면 엔터를 눌러주세요.
         
         <img title="" src="file:///Users/seongjin/Library/Application Support/marktext/images/2022-01-30-17-58-21-image.png" alt="" width="437">
      
      3. 터미널 프로그램이 실행됩니다.
         
         ![](/Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-17-58-37-image.png)
         
         <aside>
         💡 터미널은 마우스 클릭이 아닌 키보드로 컴퓨터에게 명령을 내리는 프로그램 입니다.
         
         <img src="file:///Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-17-59-11-image.png" title="" alt="" width="507">
         
         </aside>
      
      4. 바탕화면에서 `사과 아이콘` → `이 Mac에 관하여`를 클릭하여 macOS 버전을 확인해 주세요.
         
         ![](/Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-17-59-52-image.png)
      
      5. macOS 버전을 확인한 뒤, 해당하는 명령어를 복사해 주세요.
         
         <aside>
         💡 mac OS 버전 순서
         
         <img src="file:///Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-18-03-40-image.png" title="" alt="" width="464">
         
         **macOS Mojave** 이하 버전을 사용하는 경우 설정하는 파일이 다릅니다.
         
         </aside>
         
         - macOS 카타리나(Catalina) 이상 버전 명령어
           
           ```bash
           mkdir ./Developments && mv ~/Downloads/flutter ./Developments/ && echo 'export PATH="$PATH:$HOME/Developments/flutter/bin"' >> ~/.zshrc && source ~/.zshrc
           ```
         
         - macOS 모하비(Mojave) 이하 버전 명령어
           
           ```bash
           mkdir ./Developments && mv ~/Downloads/flutter ./Developments/ && echo 'export PATH="$PATH:$HOME/Developments/flutter/bin"' >> ~/.bash_profile && source ~/.bash_profile
           ```
           
           
           
           
           💡 어떤 명령어인지 궁금하신 분들은 아래 설명을 참고해 주세요.
           
           - 명령어 설명
             
             1. Developments 폴더 만들기
                
                ```bash
                mkdir ./Developments
                ```
                
                
                
             
             2. 다운로드 폴더에 있던 flutter 폴더를 Developments 폴더로 이동
                
                ```bash
                mv ~/Downloads/flutter ./Developments/
                ```
             
             3. Developments/flutter/bin 폴더에 있는 flutter 파일을 어디서든 실행할 수 있도록 등록(환경변수에 등록)
                
                > macOS 모하비 버전에서는 `.bash_profile`이라는 파일에 등록하고 이후 버전에선 `.zshrc` 파일이 등록하기 때문에 명령어가 다릅니다.
                
                ```bash
                echo 'export PATH="$PATH:$HOME/Developments/flutter/bin"' >> ~/.zshrc
                ```
             
             4. 설정 반영
                
                ```bash
                source ~/.zsh
                
                ```
             
             5. 이전 명령이 성공하면 다음 명령어를 실행하도록 &&로 연결하여 아래 명령어 완성
                
                ```bash
                mkdir ./Developments && mv ~/Downloads/flutter ./Developments/ && echo 'export PATH="$PATH:$HOME/Developments/flutter/bin"' >> ~/.zshrc && source ~/.zshrc
                ```
           6. 터미널에 단축키 `Cmd + v` 또는 마우스 우클릭하여 `붙여넣기`를 눌러주세요.
              
              ![](/Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-18-26-59-image.png)
              
              아래와 같이 붙여넣으면 아래와 같이 나오고, 엔터(enter)를 눌러 실행해 주세요.
              
              ![image](https://user-images.githubusercontent.com/55625864/151694207-955e3861-3cd0-40a7-bc6d-3216073b4854.png)
              
              만약 아래와 같은 팝업이 뜨면 `확인` 버튼을 눌러주세요.
              
              <img src="https://user-images.githubusercontent.com/55625864/151694238-d8dd14ca-5722-43a1-86fa-3b59f2d1e250.png" title="" alt="image" width="257">
           
           7. 다음 명령어는 flutter의 버전을 확인하는 명령어입니다. 아래 명령어를 복사해 주세요.
              
              ```bash
              flutter --version
              ```
              
              터미널에 붙여넣고 실행해 주세요.
              
              ![image](https://user-images.githubusercontent.com/55625864/151694246-bfe8f594-bc20-4ba1-9d7e-145ce14cb095.png)
              
              아래 8~9는 안노올 수 도 있습니다.
           
           8. 다음 팝업이 뜨면 `설치` 버튼을 눌러주세요.
              
              ![image](https://user-images.githubusercontent.com/55625864/151694275-980d8f24-8e92-4231-a708-3cad9fead9f3.png)
           
           9. 사용권 계약 팝업이 뜨면 `동의` 버튼을 눌러주세요.
              
              ![image](https://user-images.githubusercontent.com/55625864/151694291-48400745-c7b0-4675-a1ee-0a35d15b9c9f.png)
           
           10. 아래와 같이 설치가 완료되면 `완료` 버튼을 눌러주세요.
               
               ![image](https://user-images.githubusercontent.com/55625864/151694399-7b705dad-aa14-45db-9e45-074cd1056733.png)
           - 설치 확인
             
             1. 터미널 창에 Flutter 버전을 확인하는 아래 명령어를 붙여넣고 실행해 주세요.
                
                ```bash
                flutter --version
                ```
                
                실행하면 `Building flutter tool...` 이라고 출력되고 잠시 후 아래와 같이 Flutter 버전이 출력되면 Flutter 설치 완료!
                
                ![image](https://user-images.githubusercontent.com/55625864/151694399-7b705dad-aa14-45db-9e45-074cd1056733.png)
                
                💡 위 이미지에선 Flutter 2.5.3 버전이 출력되는데 시간이 지나면 최신 버전으로 업데이트 되어 버전이 다를 수 있습니다. 전혀 문제 없으니 그대로 진행해주세요.
             
             2. 다음 명령어를 복사해 터미널에 붙여넣고 실행해 주세요.
                
                💡 Flutter 개발하는데 필요한 항목들의 상태를 확인하는 명령어 입니다.
                
                ```bash
                flutter doctor
                ```
                
                ![image](https://user-images.githubusercontent.com/55625864/151694645-0cbc8647-d1ef-4404-8c85-f84f8d7ce2c2.png)
                
                - 💡 Android 앱을 만드는데 필요
                  
                  - Android Studio
                  - Android SDK
                  
                  iOS 앱을 만드는데 필요
                  
                  - Xcode
                  - CocoaPods
                
                위 프로그램들을 하나씩 설치해 보도록 하겠습니다.

- 2. **Xcode**
  
  <aside>
  💡 iOS 앱을 개발하는데 필요한 Xcode를 설치해 보도록 하겠습니다.
  
  </aside>
  
  1. [링크](https://apps.apple.com/us/app/xcode/id497799835)를 클릭해 열어주세요.
  
  2. 아래와 같은 팝업이 띄면 `App Store 열기` 버튼을 눌러주세요.
     
     ![image](https://user-images.githubusercontent.com/55625864/151694689-5af78379-b645-424b-a596-e741f3973cae.png)
  
  3. `App Store`가 실행되고 `Xcode`가 아래와 같이 뜨면 `받기` 버튼을 눌러주세요.
     
     ![image](https://user-images.githubusercontent.com/55625864/151694716-36294c01-f1be-4951-97a5-a75766e6bbf8.png)
  
  4. `설치` 버튼으로 변하면 한 번 더 눌러주세요.
     
     <img src="https://user-images.githubusercontent.com/55625864/151694758-0cda78ac-d04a-4176-b096-4da5046808aa.png" title="" alt="image" width="366">
  
  5. 만약 App Store에 Apple ID로 로그인이 되어있지 않아 아래와 같이 창이 뜨는 경우, 로그인을 진행해 주세요.
     
     <aside>
     💡 계정이 없다면 `Apple ID 생성`을 눌러 가입을 진행해주신 뒤, 로그인을 진행해 주세요.
     
     </aside>
     
     ![image](https://user-images.githubusercontent.com/55625864/151694788-3cb3bf26-401f-41f8-b042-57ce1649272d.png)
  
  6. 로그인을 완료하면 설치가 진행 됩니다.
     
     <aside>
     💡 Xcode 설치 시간은 인터넷 상황에 따라 다르지만 보통 1시간 30분 ~ 2시간 정도 소요 됩니다. 😂
     
     </aside>
  
  7. 설치가 완료되면 `열기` 버튼을 눌러주세요!
     
     <img src="https://user-images.githubusercontent.com/55625864/151694811-0ff0cf3d-45d9-4abc-b190-53c0fd9ca84d.png" title="" alt="image" width="496">
  
  8. 라이센스 동의 팝업이 뜨면 `Agree`를 선택해 주세요.
     
     <img src="https://user-images.githubusercontent.com/55625864/151694829-8f636c95-13de-4aa9-a908-eb7ccafaeec6.png" title="" alt="image" width="446">
  
  9. 아래와 같이 암호를 입력하는 창이 뜨면 컴퓨터 시작 비밀번호를 입력한 뒤 `확인` 버튼을 눌러주세요.
     
     <img src="file:///Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-18-51-05-image.png" title="" alt="" width="288">
  
  10. 만약 Xcode가 실행이 안되면, 다시 `열기` 버튼을 눌러주세요.
      
      <img src="https://user-images.githubusercontent.com/55625864/151694885-73728a2b-71de-44a6-b474-81586b3bf070.png" title="" alt="image" width="462">
  
  11. 아래와 같은 창이 뜨면 Xcode 설치완료!
      
      ![image](https://user-images.githubusercontent.com/55625864/151694913-90f807a9-9185-4faa-8888-28e5afc582fa.png)
  
  12. 설치를 완료했으니`AppStore`와 `Xcode`를 종료해 주세요.
      
      - 하단에 App Store를 우클릭하여 `종료`를 선택해 주세요.
        
        <img title="" src="https://user-images.githubusercontent.com/55625864/151694972-a26b9808-6351-4336-bc3c-0c4e61557eb8.png" alt="image" width="382">
      
      - 하단에 Xcode를 우클릭하여 `종료`를 선택해 주세요.
        
        <img src="https://user-images.githubusercontent.com/55625864/151694995-8d55966c-5ad5-444f-b859-70d8d4cdf496.png" title="" alt="image" width="492">
  
  13. 다음으로 CocoaPods을 설치해 보도록 하겠습니다.
      
      <aside>
      💡 CocoaPods은 다른 사람이 만든 코드를 가져올 때 필요한 프로그램으로 Xcode와 함께 iOS 앱 개발시 필요합니다.
      
      </aside>
      
      아래 명령어를 복사해 터미널에서 붙여넣고 엔터를 눌러주세요.
      
      ```bash
      sudo gem install cocoapods
      ```
  
  14. 아래와 같이 비밀번호를 입력하는 창이 나오면, 컴퓨터 시작시 입력하는 비밀번호를 입력한 뒤 엔터를 눌러주세요.
      
      <aside>
      💡 참고로 키보드를 눌러도 화면에 입력되는 모습은 보이지 않으니, 입력한 뒤 엔터를 누르면 됩니다.
      
      비밀번호를 틀린 경우, `Ctrl + C`를 누르면 명령이 종료되고, 다시 명령어를 붙여넣고 실행해주세요.
      
      </aside>
      
      <img src="https://user-images.githubusercontent.com/55625864/151699764-d58c720a-2e6c-4c46-b693-80dc6e97ee55.png" title="" alt="image" width="489">
  
  15. 명령이 정상적으로 실행되면 아래와 같이 `** gems installed`라고 뜹니다.
      
      <img src="https://user-images.githubusercontent.com/55625864/151699802-4e7277ce-feb6-425d-8db4-8101bb069a01.png" title="" alt="image" width="565">
  
  16. 아래 명령어를 복사해 터미널에서 실행해 주세요.
      
      ```bash
      flutter doctor
      ```
      
      그러면 아래와 같이 `Xcode` 설치가 완료된 것을 보실 수 있습니다.
      
      ![image](https://user-images.githubusercontent.com/55625864/151699876-b6a8fd2d-cad4-4d56-b8a4-c910d70a4175.png)

- 3. **Android Studio**
  - **Android Studio 설치**
    
    1. [링크](https://developer.android.com/studio)를 클릭해서 접속해주세요.
    
    2. 아래와 같이 화면이 나오면 `Download Android Studio` 버튼을 눌러주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151700011-363e258a-b1c5-49b9-baf5-18e4d77bcdec.png)
    
    3. 약관이 뜨면 아래로 쭉 스크롤 해주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151700061-f8b0c113-e09f-466c-a116-9e715c988621.png)
    
    4. Intel 칩을 사용하는 맥북은 왼쪽 `Mac with Intel chip`을 Apple 칩을 사용하는 맥북은 오른쪽 `Mac with Apple chip`을 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151700096-a46f8c95-48b1-440e-8d92-1954ecb08dd7.png)
       
       <aside>
       💡 좌측 상단 `Apple 로고` 클릭 → `이 Mac에 관하여`를 클릭하여 Intel 칩인지 Apple 칩인지 확인할 수 있습니다.
       
       - Intel chip
         
         <img title="" src="https://user-images.githubusercontent.com/55625864/151700182-75a1d38a-4549-4e46-b5d3-1d4cbe18f02d.png" alt="image" width="512">
       
       - Apple chip
         
         <img src="https://user-images.githubusercontent.com/55625864/151700187-c49011eb-ce38-4b1c-adb1-f2e006c4c468.png" title="" alt="image" width="488">
    
    5. 다운로드 팝업이 뜨면 `저장` 버튼을 눌러주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151700711-816e4f13-0e7f-4c44-8fda-afc30c188dce.png" title="" alt="image" width="398">
    
    6. 바탕화면 하단에 휴지통 좌측에 있는 `다운로드` 폴더를 클릭한 뒤 `Finder`에서 열기 버튼을 클릭해 주세요.
       
       <img title="" src="https://user-images.githubusercontent.com/55625864/151700731-1564154c-e91b-4ae0-889b-8ae6cf10cd80.png" alt="image" width="415">
    
    7. 다운로드가 완료된 `android-studio~~.dmg` 파일을 실행해 주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151700778-5b28a7f0-abc8-4ce6-8eae-e58feac8fdb3.png" title="" alt="image" width="500">
    
    8. 아래와 같은 창이 뜨면 왼쪽에 `Android Studio`를 드래그해서 `Applications`에 떨어뜨려주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151700880-a92e1185-966d-487b-8db9-572233e90484.png" title="" alt="image" width="418">
    
    9. 설치가 완료되면 좌측 상단에 빨간 X를 눌러서 아래 화면을 종료해 주세요.
       
       <img src="file:///Users/seongjin/Library/Application%20Support/marktext/images/2022-01-30-22-05-25-image.png" title="" alt="" width="438">
       
       <aside>
       💡 바탕화면에 아래 사진과 같은 파일이 생겼다면 휴지통으로 드래그해 삭제하셔도 됩니다.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701015-c2d81137-1bbf-47ed-bd7c-cca41149ca70.png)
    
    10. 우측 상단에 `돋보기🔍` 아이콘을 클릭하고, 팝업창이 뜨면 `android`라고 입력해 주세요. 그리고 아래와 같이 `Android Studio`가 자동완성으로 뜨면 엔터를 눌러 실행해 주세요.
        
        </aside>
        
        ![image](https://user-images.githubusercontent.com/55625864/151701030-d8d2f5e5-173d-4fcd-9955-d47157eccab1.png)
    
    11. 아래와 같이 팝업이 뜨면 `열기` 버튼을 눌러주세요.
        
        <img title="" src="https://user-images.githubusercontent.com/55625864/151701082-cacddd83-5710-4830-82a3-8f3f787632e8.png" alt="image" width="289">
    
    12. 아래와 같은 창이 뜬다면 `OK` 버튼을 눌러주세요.
        
        <img src="https://user-images.githubusercontent.com/55625864/151701092-08855880-4214-4093-973b-7be30a40e09b.png" title="" alt="image" width="239">
    
    13. `Import Android Studio Settings` 팝업이 뜨면 `Do not import settings`를 선택하신 뒤 `OK` 버튼을 눌러주세요.
        
        
        <img src="https://user-images.githubusercontent.com/55625864/151701148-839234c5-9313-452b-94af-cbc6d5b31198.png" title="" alt="image" width="411">
        
    
    14. 안드로이드 스튜디오 사용 데이터를 구글에 전달하여 사용성 개선에 참여하고 싶다면 `Send usage statistics to Google`을 선택해주시고, 그렇지 않은 경우 `Don't send`를 선택해 주세요.
        
        <img src="https://user-images.githubusercontent.com/55625864/151701177-96cf756f-fab0-4df4-a76f-d14312329feb.png" title="" alt="image" width="445">
    
    15. 다음과 같은 안드로이드 스튜디오 설정 화면이 나오면 `Next` 버튼을 눌러주세요.
        
        <img src="https://user-images.githubusercontent.com/55625864/151701203-9060743f-edbf-4fc9-8af2-bd7083e3c78d.png" title="" alt="image" width="460">
        
        <img src="https://user-images.githubusercontent.com/55625864/151701214-a8203741-c02c-4ce8-9056-8fe008b474c1.png" title="" alt="image" width="464">
        
        <img src="https://user-images.githubusercontent.com/55625864/151701297-1820d08a-0dd4-4946-961f-a53413d10545.png" title="" alt="image" width="468">
    
    16. `Finish` 버튼을 눌러 Android SDK 설치를 진행해 주세요.
        
        ![image](https://user-images.githubusercontent.com/55625864/151701510-51988fb5-2b60-40b7-8fbc-3834ee1446d4.png)
    
    17. 설치가 완료되면 `Finish` 버튼을 눌러주세요.
        
        ![image](https://user-images.githubusercontent.com/55625864/151701501-1af7764b-280a-45ef-935f-cfcd54e170cd.png)
    
    18. 아래와 같은 화면이 뜨면 Android Studio 설치 완료!
        
        ![image](https://user-images.githubusercontent.com/55625864/151701542-415b92d3-d3ad-42bf-b259-3332a3c976c6.png)
  
  - **Android Command-line Tools 설치**
    
    <aside>
    💡 `Android Command-line Tools`는 Flutter에서 Android에 명령을 내리기 위해 필요합니다.
    
    </aside>
    
    1. Android Studio에서 `More Actions`를 선택한 뒤 `SDK Manager`를 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701629-8d5975ff-607b-4259-b713-c9bcddce521d.png)
    
    2. 그러면 아래와 같이 `Preferences for New Projects` 팝업이 뜨면 `SDK Tools` 탭을 선택 → `Android SDK Command-line Tools (latest)` 선택 → `Apply` 를 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701661-595ff95f-a552-454b-9a2b-db40c06feec2.png)
    
    3. 팝업이 뜨면 `OK` 버튼을 클릭해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701787-93c58726-2402-4314-ad07-da7d5bf54dd4.png)
    
    4. 라이센스에 `Accept`를 선택하여 동의하고 `Next`를 선택하여 설치를 진행해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701839-31b8aaad-34aa-4b76-a1b9-e46dd3d7a22b.png)
    
    5. 설치가 완료되면 `Finish` 버튼을 눌러주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701859-a9b44fe8-25a4-4dce-900a-497ea7dfe23b.png)
    
    6. `OK` 버튼을 눌러주시면 설치 완료!
       
       ![image](https://user-images.githubusercontent.com/55625864/151701897-4409965a-0817-48b0-9e2f-693e6bcd85f3.png)
  
  - **Android Virtual Devices 설치**
    
    <aside>
    💡 앱을 개발시 실제 휴대폰을 연결하여 개발을 진행할 때도 있지만, 대부분의 경우 Virtual Device(컴퓨터에 가상의 휴대폰을 띄우는 소프트웨어)를 이용하여 개발합니다.
    
    </aside>
    
    1. Android Studio에서 `More Actions`를 클릭한 뒤 `AVD Manager`를 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701943-0dd4bdf6-cc10-4c1a-9d64-aed66535c876.png)
    
    2. `Create Virtual Device...`를 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701967-75756b8e-035b-4d24-8519-d07e7d054a28.png)
    
    3. 하드웨어를 선택하는 화면이 나오면 `Next`를 눌러서 기본으로 설정된 `Pixel 2` 휴대폰을 설치하도록 하겠습니다.
       
       ![image](https://user-images.githubusercontent.com/55625864/151701993-2d5d5cf6-a9cc-48a4-a551-77831fbebeac.png)
    
    4. 휴대폰에 설치할 Android OS를 선택하는 화면입니다. `Q` 옆에 있는 `Download` 버튼을 클릭하여 OS를 다운로드해 주세요.
       
       <aside>
       💡 R 버전은 Virtual Device에서 문제가 있다고 해요. 그래서 **Q 버전**으로 진행할게요!
       
       </aside>
       
       <img title="" src="https://user-images.githubusercontent.com/55625864/151702033-1dbdd8b0-4d84-47e7-991d-cdc5a22fb14f.png" alt="image" width="593">
    
    5. 설치가 완료되면 `Finish` 버튼을 눌러주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151702053-e1e8b04e-6c27-4162-b3d5-f6f668ada05e.png" title="" alt="image" width="519">
    
    6. `Q` 옆에 `Download` 버튼이 사라졌습니다. 우측에 현재 선택된 OS 버전이 29인지 확인한 뒤 `Next` 버튼을 눌러주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151702064-6648067c-e2f9-491e-bcf1-4e853f558c95.png" title="" alt="image" width="526">
    
    7. `Finish` 버튼을 눌러 Virtual Device 설치를 완료해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702097-85b3de0b-2644-4ff7-9f2f-24e3c98e6071.png)
    
    8. 아래와 같이 `Pixel 2 API 29` 라는 Virtual Device가 추가되었습니다.
       
       이제 좌측 상단에 빨간 버튼을 눌러 창을 종료해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702256-2c65ae9d-3720-42f6-a65e-2aeb2f6e0778.png)
    
    9. 하단에 Android Studio 아이콘을 우클릭한 뒤 `종료` 버튼을 눌러를 Android Studio를 종료해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702256-2c65ae9d-3720-42f6-a65e-2aeb2f6e0778.png)
       
       <aside>
       💡 Android Studio를 클릭한 상태에서 단축키(`Cmd + Q`)를 누르셔도 됩니다.
       
       </aside>
       
       - 4. Android Licenses
         
         5. 터미널에서 `flutter doctor`라고 입력한 뒤 엔터를 누릅니다.
            아래와 같이 `Android toolchain`의 좌측에 `[!]` 표시가 되어있습니다.
            
            ![image](https://user-images.githubusercontent.com/55625864/151702592-1ed81b2a-b5d2-4553-8bd4-ae5dac9ffe12.png)
         
         6. 문제를 해결하기 위해 `flutter doctor --android-licenses`를 복사해서 터미널에 붙여 넣고 실행해 주세요. 실행시 라이센스에 대한 동의를 여러번 구하는데, `y`를 입력하고 엔터를 눌러 진행해 주세요.
            
            ![image](https://user-images.githubusercontent.com/55625864/151702615-d3de50e5-3d48-4dcb-bc47-80de2af87e7d.png)
         
         7. 모든 동의가 완료되면 `All SDK package licenses accepted` 라고 뜹니다.
            
            ![image](https://user-images.githubusercontent.com/55625864/151702617-719ede86-a73a-484c-84dd-28bef745637c.png)
         
         8. 마지막으로 터미널에 `flutter doctor` 를 입력했을 때 아래와 같이 모든 항목이 체크 완료되면 완료!
            
            ![image](https://user-images.githubusercontent.com/55625864/151702618-738cdf23-5f06-4fe2-a3e5-259fb0f0356e.png)

- **Visual Studio Code**
  
  <aside>
  💡 Visual Studio Code (줄여서 VSCode) 앞으로 실제 코드를 작성할 편집 툴입니다.
  
  Flutter 개발은 Android Studio와 VSCode 둘 중 원하는 툴을 사용하여 개발할 수 있는데 VSCode가 더 가볍기 때문에 앞으로 수업은 VSCode에서 진행하도록 하겠습니다.
  
  </aside>
  
  - VSCode 설치
    
    1. [링크](https://code.visualstudio.com/download)에 접속해 주세요.
    
    2. Mac 하단에 버튼을 클릭해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702877-05e227d2-4ff1-4c60-80fb-f900c3be2f12.png)
    
    3. `다운로드` 폴더에 저장해 주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151702878-25e00924-aaef-492a-9885-42995543d22a.png" title="" alt="image" width="398">
    
    4. 바탕화면에 다운로드 폴더를 클릭한 뒤 `Finder에서 열기` 버튼을 클릭해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702884-c04f87e7-a3b7-40fa-a778-b946ae3bde07.png)
    
    5. 다운받은 `VSCode-darwin-universal.zip` 파일을 실행해 압축을 풀어주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702886-267f1b91-6699-4cc0-8d05-993b97dbed88.png)
    
    6. 압축이 풀리고 생성된 `Visual Studio Code` 파일을 드래그해서 왼쪽 `응용 프로그램`에 떨어뜨려 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702888-9a04a199-2b1e-457f-bf89-7d454ec5e3dd.png)
    
    7. 화면 우측 상단 `돋보기 🔍` 아이콘을 클릭한 뒤 `visual` 이라고 검색해 주세요. 그리고 하단에 `Visual Studio Code`가 보이면 엔터를 눌러 실행해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151702890-507bf9cd-3cd0-45af-a330-83c56e747119.png)
    
    8. 아래와 같은 팝업이 뜨면 `열기` 버튼을 눌러주세요.
       
       <img src="https://user-images.githubusercontent.com/55625864/151702895-1ad10448-f351-4299-9243-e594fd3bd879.png" title="" alt="image" width="232">
    
    9. 그러면 아래와 같이 VSCode가 실행되면 설치 완료!
       
       ![image](https://user-images.githubusercontent.com/55625864/151702899-ab877767-e8ca-465a-9a3d-3446a7b34c83.png)
       
       <aside>
       💡 우측 하단에 한국어로 변경하는 팝업이 뜨는데, VSCode 사용법을 인터넷에 검색시 대부분의 자료가 영어로 되어 있기 때문에, 가급적 적용하지 않기를 권장 드립니다. (수업 자료도 영어 버전으로 되어있어요!)
       
       해당 알람을 다시는 보지 않으려면 `우측 톱니바퀴 ⚙` 아이콘을 누른 뒤 `Don't Show Again`을 선택해 주세요. (만약 사라져서 버튼을 누르지 못했다면 다음번에 눌러주세요!
       
       ![image](https://user-images.githubusercontent.com/55625864/151703079-4609a466-fdff-4f1d-a0a0-37d9bab305e5.png)
       
       </aside>
  
  - 2. Extension 설치
    
    <aside>
    💡 VSCode는 Flutter 뿐만 아니라 다양한 개발을 모두 할 수 있는 통합 에디터입니다. VSCode에서 Flutter 앱 개발을 하려면 VSCode에 Extension 탭에서 아래 목록의 Extension 들을 설치해야 합니다.
    
    Flutter : VSCode에서 Flutter 개발 환경 지원
    Dart : Flutter 개발 시 사용되는 Dart 개발 환경 지원
    Awesome Flutter Snippets : Flutter 개발 시 자주 쓰이는 코드 자동 완성 지원
    
    </aside>
    
    1. 좌측에 extension 아이콘(주황 동그라미)을 선택해 주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151703177-3863bd1c-4c83-4e4b-a9f3-8963f01edf91.png)
    
    2. `flutter` 라고 검색한 뒤, 해당 첫 번째 항목을 선택하고 `install` 버튼을 눌러 설치해주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151703186-df019360-1170-434c-ad77-a1a5d7130ae1.png)
    
    3. 바로 아래에 있는 `Awesome Flutter Snippets` 익스텐션도 설치해주세요.
       
       ![image](https://user-images.githubusercontent.com/55625864/151703182-bd7de53e-0beb-48cf-8d5e-e1d1edda7d06.png)
    
    4. `dart` 라고 검색하신 뒤, 해당 익스텐션을 설치해주세요. 만약 `uninstall`이라고 뜨신다면 이미 설치가 되셨으니 넘어가시면 됩니다.
       
       ![image](https://user-images.githubusercontent.com/55625864/151703189-33137c47-9f9a-44b3-b2ac-ed98e1ec5738.png)
       
       모든 설치가 완료 되었습니다!

- 최종 설치 확인
  
  터미널에서 `flutter doctor`라고 검색한 뒤 아래와 같이 화면이 나온다면 모든 설치가 완료하신 것입니다.
  
  ![image](https://user-images.githubusercontent.com/55625864/151703192-da9eb9c7-6980-4066-99e7-e244881c63b6.png)
  
  <aside>
  💡 다운로드 폴더에 있는 파일들은 모두 삭제하셔도 됩니다.
  
  </aside>
  
  <aside>
  💡 고생하셨습니다! 원래 개발 환경을 설정하는데 시간이 많이 들어갑니다 😂
  그럼 1주 차 수업 때 뵙도록 하겠습니다 🙂
  
  </aside>




