# flutter 앱을 만들기 위해 알아야되는 개념들

## 프로젝트 초기화
두개의 dart파일을 통해서 프로젝트 구조를 조금 파악해보고 시작해보자
```dart
// lib/screen/home_screen.dart
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  
  // const 생성자
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Text('Home Screen');
    );
  }
}

// lib/main.dart
import 'package:my_app/screen/home_screen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: HomeScreen(),
    ),
  );
}
```
코드를 맨 위부터 천천히 뜯어보자.
> import 'package:flutter/material.dart';

이 코드는 Material Design 위젯들을 사용하기 위해 쓴다. Material Design은 구글이 만든 디자인 시스템으로, 플러터에서는 이걸 사용해서 다양한 UI를 만들 수 있다.

> class HomeScreen extends StatelessWidget 

HomeScreen 이라는 클래스를 만들었다. 이 클래스는 플러터에서 제공하는 StatelessWidget을 상속받고 있다. StatelessWidget은 한 번 화면이 그려지면 상태가 변하지 않는 위젯이다. 즉, 화면의 데이터가 변하지 않으면 계속 같은 UI를 보여준다.

> const HomeScreen({Key? key}) : super(key: key);

const 키워드를 사용해서 생성자를 만들었다.  
생성자는 클래스를 새로 만들 때 실행되는 함수라고 보면 된다.  
const는 생성된 객체가 변하지 않는다는 뜻이다. 즉, 이 클래스를 계속해서 같은 값으로 사용할 수 있다.  
*super* 가 엄청 자주 나오는데 대체 뭘까 ? super가 하는 역할은 부모 클래스의 생성자를 호출하는 것이다. 자세히 설명해보면,
- HomeScreen 클래스는 StatelessWidget을 상속받고 있다. 즉, HomeScreen은 StatelessWidget이라는 부모 클래스의 기능을 물려받는 것.
- 상속받은 클래스는 부모 클래스의 생성자를 호출해야 하는데, 이때 super 키워드를 사용한다.
- 여기서 StatelessWidget 부모 클래스는 const StatelessWidget({Key? key})라는 생성자를 가지고 있다. 그래서 super(key: key)를 호출해서 부모 클래스의 생성자를 실행하고, 전달받은 key 값을 부모 클래스에 전달하는 것이다.

왜 super을 써야할까?
- 부모 클래스(StatelessWidget)가 내부적으로 필요한 설정이나 초기화 작업을 할 수 있게 해준다
- super를 호출하지 않으면 부모 클래스의 생성자를 건너뛰게 되므로, 부모 클래스의 기능이 제대로 동작하지 않을 수 있다.

> @override  
> Widget build(BuildContext context)

- @override는 상속받은 StatelessWidget 클래스의 build 함수를 재정의한다는 의미이다.
- build 함수는 플러터에서 위젯의 모양을 그리는 함수이다.
- build 함수의 매개변수로 들어가는 BuildContext는 플러터에서 화면 위젯 트리와 관련된 정보를 가지고 있는 객체이다. 간단히 말하면, 현재 위젯이 앱의 전체 UI 트리에서 어디에 위치해 있는지를 나타내는 정보이다.

> return Scaffold(
> body: Text('HomdeScreen');
> );

- Scaffold는 화면을 만들기 위한 뼈대를 제공한다. 화면의 기본 구조를 잡아준다고 보면 된다.
- body 속성은 화면의 주요 콘텐츠를 표시하는 부분이다.

> void main()

- main 함수는 플러터 앱이 실행될 때 제일 처음 호출되는 함수이다.

> runApp( MaterialApp (),);

- runApp 함수는 플러터 앱을 시작하는 함수이다.
- MaterialApp은 앱 전체에 Material Design을 적용해주는 역할을 한다

대체 flutter을 하다보면 어디는 return Scaffold, 어디는 return Material
## StatelessWidget

위젯의 형태는 2가지로 나뉜다.
- StatefulWidget : 위젯의 내부에서 값이 변경되었을 때 위젯 자체에서 다시 렌더링을 실행시킬 수 있는 위젯
- StatelessWidget : 위젯 내부에서 값이 변경되어도 위젯 자체적으로는 다시 렌더링할 수 없는 위젯

### StatelessWidget 실습 : StatelessWidget 틀 살펴보기
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());  // 1. SplashScreen 위젯을 첫 화면으로 지정
}

class SplashScreen extends StatelessWidget {  // 2. StatelessWidget 선언
  @override
  Widget build(BuildContext context) {  // 3. 위젯의 UI 구현
    
  }
}
```
위는 기본적인 StatelessWidget의 틀이다.  
플러터에서 기본으로 제공하는 StatlessWidget이라는 클래스를 사용자 정의 위젯(SplashScreen)이 상속받으면 된다.  
그러면 build()함수를 필수적으로 오버라이드하게 되는데 화면에 그려주고 싶은 위젯을 입력하면 된다.
- override는 왜 쓰지 ? 복습해보자. override는 부모 클래스 또는 인터페이스에 정의된 메서드를 재정의할 때 사용된다.
- build() 함수는 뭐지 ? override 메서드인 build 메서드는 구현한 UI 위젯들을 화면에 출력될 수 있도록 리턴해준다.

그럼 실습을 더 진행해보자.
### StatelessWidget 실습 : 화면 중앙에 Splash Screen 글씨 띄우기
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(  // 1. 항상 최상단에 입력되는 위젯
      home: Scaffold(   // 2. 항상 두 번째로 입력되는 위젯
        body: Center(   // 3. 중앙 정렬 위젯
          // 4. 글자를 화면에 보여주는 위젯
          child: Text('Splash Screen'),
        ),
      ),
    );
  }
}
```

### StatelessWidget 실습 : 배경색 바꾸기
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(  // 컨테이너 위젯
          // 컨테이너를 디자인하는 클래스
          decoration: BoxDecoration(
            color: Colors.orange,   // 색상
          ),
          child: Center(
            child: Text('Splash Screen'),
          ),
        ),
      ),
    );
  }
}
```

### StatelessWidget 실습 : 이미지 출력하기 with Image 위젯
Image 위젯은 다음과 같이 다섯 가지 생성자가 있다
1. 기본 Image 생성자는 ImageProvider라는 또 다른 위젯에서 이미지를 그립니다.
2. Image.asset 생성자는 앱에 저장된 asset 파일로 이미지를 그립니다.
3. Image.network 생성자는 URL을 통해서 이미지를 그립니다.
4. Image.file 생성자는 파일을 통해서 이미지를 그립니다.
5. Image.memory 생성자는 메모리에서 직접 이미지를 그립니다.

아래 실습에서는 Image.asset을 사용해서 실습을 할 것이다.
1. 프로젝트에서 assets 폴더를 생성한다.
2. assets 폴더에 이미지를 저장한다.
3. pubspec.yaml 파일에 들어가서 flutter.assets라는 키에 assets 폴더를 지정한다
```dart
flutter:

uses-material-design: true
assets:
  - assets/
```
4. 위 설정이 끝났으면 flutter pub get 명령어를 통해 설정을 저장한다.
5. 실습을 진행한다
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(  // 컨테이너 위젯
          // 컨테이너를 디자인하는 클래스
          decoration: BoxDecoration(
            color: Colors.orange,   // 색상
            // 아래와 같이 Color를 헥스 코드를 변환할 수 있다.
            // color: Color(0xFFF99231),
          ),
          child: Center(
            // 1. Text 위젯을 Image 위젯으로 변경
            child: Image.asset(
              'assets/logo.png',
            ),
          ),
        ),
      ),
    );
  }
}
```

### StatelessWidget 실습 : Row & Column 위젯

애니메이션 위젯으로는 LinearProgressIndicator와 CircularProgressIndicator가 있다.  
로고 아래에 동그라미 형태의 로딩 애니메이션을 사용하는데 Center위젯은 child에 위젯을 하나만 받을 수 있다. 어떻게 Image위젯과 CircularProgressIndicator 위젯을 모두 가운데 정렬할 수 있을까.  

Row와 Column위젯을 쓰면 된다. Row는 가로 Column은 세로를 의미한다. Center위젯은 child에 하나의 위젯만 받을 수 있지만 Row와 Column위젯은 children 매개변수에 리스트로 원하는 만큼 위젯을 추가할 수 있다.

코드를 너무 나열하면 길어서 실습 순서대로 진행해주세요 (주석에 써있는 1, 2, 3... 순서대로)

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          decoration: BoxDecoration(
            color: Color(0xFFF99231),
          ),
          child: Column(
            // 2. 가운데 정렬 추가
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // 1. 여러 위젯을 입력할 수 있는 children 매개변수
              Image.asset(
                'assets/logo.png',
                width: 200,  // 3. 너비 추가
              ),
              CircularProgressIndicator(),
            ],
          ),
        ),
      ),
    );
  }
}
```
1. Column은 children 매개변수를 사용하니 리스트 안에 위젯들을 보여주고 싶은 순서대로 입력해야 한다. 코딩한 위젯 순서대로 로고가 먼저 나오고 로딩 위젯이 아래에서 빙글빙글 도는 걸 볼 수 있다. 하지만 Center위젯과 다르게 로고가 맨 위로 갔다. 그러면 어떻게 할까
2. mainAxisAlignment 매개변수를 이용해서 children에 포함된 위젯들을 재배치할 수 있다. mainAxisAlignment 매개변수에는 MainAxisAlignment라는 enum값이 들어가는데 먼저 가운데를 의미하는 MainAxisAlignment.center를 적용한다.
3. 로고 이미지의 크기를 조금 줄여본다. 이미지 크기 조절에는 Image 위젯의 width또는 height 매개변수를 사용한다. 그런데 이렇게 적용하면 주황색 배경도 통째로 작아진다. Column의 경우 세로로 최대한 크기를 차지하는 특성이 있다. 하지만 가로로는 최소한 크기만 차지한다. 현재 Column 위젯 안에 Image 위젯과 CircularProgressIndicator 위젯만 존재하고 둘 중 더 큰 위젯인 Image위젯이 가로로 200 픽셀만큼 차지하고 있기 때문에 Column 위젯 또한 가로로 200픽셀만 차지한다.
4. Row 위젯은 Column 위젯가 정확히 반대로 작동한다. 

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(SplashScreen());
}

class SplashScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(
          decoration: BoxDecoration(
            color: Color(0xFFF99231),
          ),
          child: Row(
            // 1. Row 위젯을 사용한다.
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Image.asset(
                    'assets/logo.png',
                    width: 200,
                  ),
                  CircularProgressIndicator(
                    // 2. animate 색상을 흰색으로 변경
                    valueColor: AlwaysStoppedAnimation(
                      Colors.white,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      );
    ),
  }
}
```
## Firebase

파이어베이스는 구글이 인수한 모바일 앱 개발에 최적화된 기능을 제공하는 서비스이다. 플러터뿐만 아니라 다른 앱 개발 프레임워크 그리고 웹이나 서버에서도 이요할 수 있다.

주요 기능
|       **이름**        | **기능** |
| :-------------------: | :--------: |
| Authentication | 소셜 인증, 이메일 인증, 핸드폰 인증 등의 기능을 쉽게 연동하도록 해줍니다. |
| App Check | 보안 기능으로 허가되지 않은 클라이언트가 API 요청을 해 리소스를 낭비하는 걸 막을 수 있다. |
| Firestore | 실시간으로 클라이언트와 서버의 데이터를 연동할 수 있고 강력한 쿼리 기능을 제공해주는 NoSQL 데이터베이스이다. |
| Realtime Database | 파이어스토어와 비슷한 NoSQL 데이터베이스 기능을 제공한다. 빠른 속도와 효율에 초점이 맞춰져 있다. |
| Storage | 이미지, 오디오, 비디오 등 사용자가 생성하는 콘텐츠를 저장할 수 있는 저장소이다. |
| Hosting | 웹 앱, 정적 및 동적 콘텐츠, 마이크로서비스를 빠르고 안정적으로 호스팅할 수 있다. |
| Functions | 파이어베이스 또는 HTTPS 요청에 의해 서버 코드를 실행할 수 있는 기능이다. 트래픽에 따라 필요한 만큼 자동으로 확장되기 때문에 인프라 관리가 필요 없다. |
| Machine Learning | 간단한 몇 줄의 코드만으로 텍스트 인식, 이미지 라벨링, 물체 감지 및 추적, 얼굴 감지 및 윤곽 추적 등 머신러닝 기능을 사용할 수 있다. |
| Remote Config | 앱의 동작 모양과 기능을 앱을 새로 배포하지 않고도 변경하도록 편의성 기능을 제공해준다. |
| Crashlytics | 앱에 충돌이 있을 경우 정확한 문제와 로그를 파악할 수 있는 기능이다 |
| Performance | 앱 성능을 모니터링할 수 있는 기능이다. |
| Test Lab | 구글 데이터 센터에 실행되고 있는 여러 실제 프로덕션 기기를 사용해 앱을 테스트할 수 있다. |
| App Distribution | 앱을 더 빠르고 쉽게 배포할 수 있다. |
| Analytics | 앱의 트래픽과 활동 들을 모니터링하고 분석할 수 있다. |
| Messaging | 푸시 알림을 쉽게 설정할 수 있다. |

### firestore

Firebase의 기능 중 하나인데 NoSQL 데이터베이스이다.


## 사전 지식 정리 !

### 콜백 함수

콜백함수는 일정 작업이 완료되면 실행되는 함수이다. 함수를 정의해두면 바로 실행되지 않고 특정 조건이 성립될 때 실행되기 때문에 이름이 콜백이다. 예를 들어 유저가 화면을 터치 했을 때 실행할 함수나 웹뷰의 로딩이 완료되면 실행할 콜백 함수를 다음과 같이 정의할 수 있다.
```dart
WebViewController controller = WebViewController()
  ..setNavigationDelegate(NavigationDelegate(
    // 1. 로딩 완료 후 실행되는 함수
    onPageFinished: (String Url) {
      print(url); 
    }
  ))
```

### 웹뷰 위젯

### 안드로이드 ios 네이티브 설정

다트 언어만 사용해서 모든 작업을 할 수 있다면 매우 편하겠지만 플러터 또한 각 네이티브 플랫폼으로 코드가 컴파일 되므로 최소한의 네이티브 설정은 필요하다. 예를 들어 http, https, 인터넷 권한, 카메라, 사진첩, 푸시 권한 등 보안에 민감한 사항이나 하드웨어에 접근할 때도 네이티브 설정을 해야한다.

## 블로그 웹 앱 실습

- 프로젝트 이름 : blog_web_app
- 네이티브 언어 : 코틀린, 스위프트

### pubspec.yaml 설정하기
pubspec.yaml 파일은 플러터 프로젝트와 관련되 설정을 하는 파일이다. 프로젝트에서 사용할 이미지 및 폰트를 지정하거나 사용할 오픈 소스 프로젝트들을 명시할 때 사용된다.

1. webview_flutter 플로그인을 pubspec.yaml 파일에 추가하고 flutter pub get을 실행한다
```dart
dependencies:
  flutter:
    sdk: flutter

// 버전은 알아서 잘 찾아서 설정하시길 바랍니다 ^^
cupertino_icons: ^1.0.2
webview_flutter: 4.4.1
```

> 주요 pub 명령어 모음

|       **명령어**        | **설명** |
| :-------------------: | :--------: |
| flutter pub | pubspec.yaml 파일에 등록한 플러그인들을 내려받습니다. |
| flutter pub add [플러그인 이름] | pubspec.yaml에 플러그인을 추가합니다. 명령어의 끝에 플러그인 이름을 추가하면 됩니다. |
| flutter pub upgrade | pubspec.yaml에 등록된 플러그인들을 모두 최신 버전으로 업데이트합니다|
| flutter pub run | 현재 프로젝트를 실행합니다. 명령어를 실행하면 어떤 플랫폼에서 실행할지 선택할 수 있습니다. |

### 권한 및 네이티브 설정
웹뷰를 사용하려면 몇 가지 네이티브 설정이 필요하다. 인터넷 사용 권한을 추가하고 https 프로토콜뿐만 아니라 http 프로토콜도 이용할 수 있게 수정한다. 안드로이드와 ios 각각 설정을 해줘야한다.

#### 안드로이드 설정
1. 안드로이드 설정 파일은 android/app/src/main/AndroidManifest.xml 이다. 안드로이드 앱에 필요한 각종 권한을 여기서 설정할 수 있다.
2. 웹뷰를 실행할 때 인터넷을 사용해야 하니 인터넷 권한을 추가한다
```dart
// android/app/src/main/AndroidManifest.xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.blog_web_app">
    <uses-permission android:name="android.permission.INTERNET" />
// 생략
</manifest>
```

- 자주 사용하는 안드로이드 권한 코드
|       **코드**        | **설명** |
| :-------------------: | :--------: |
| INTERNET | 인터넷 사용 권한 |
| CAMERA | 카메라 사용 권한 |
| WRITE_EXTERNAL_STORAGE | 앱 외부에 파일을 저장할 수 있는 권한 |
| VIBRATE | 진동을 일으킬 수 있는 권한 |
| ACCESS_FINE_LOCATION | GPS와 네트워크를 모두 사용해서 정확한 현재 위치 정보를 가져올 수 있는 권한 |
| ACCESS_COARSE_LOCATION | 네트워크만 사용해서 대략적인 위치 정보를 가져올 수 있는 권한 |
| ACCESS_BACKGROUND_LOCATION | 앱이 배경에 있을 때 위치 정보를 얻을 수 있는 권한 |
| BILLING | 인앱 결제를 할 수 있는 권한 |
| CALL_PHONE | 전화기 앱을 사용하지 않고 전화를 할 수 있는 권한 |
| NETWORK_STATE | 네트워크 상태를 가져올 수 있는 권한 |
| RECORD_AUDIO | 음성을 녹음할 수 있는 권한 |

## 강의 정리

### 단축키

- stf + tab : StatefulWidget 생성
- stl + tab : StatelessWidget 생성

### 용어
- scafford : 뼈대라는 뜻이다. 플러터에서 보여지는 화면의 뼈대를 구성할 때 주로 쓴다.
  - appbar
  - drawer
  - body
  - floatingActionButton