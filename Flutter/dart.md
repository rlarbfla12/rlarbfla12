> Dart가 처음인 사람들은 꼭 처음부터 끝까지 예시 코드 제가 정성스레 작업한 것 이니까 DartPad에서 실습 진행하세요 !
> 작성자 : 이상무

## 1.1 다트 소개

- 다트 언어는 UI를 제작하는 데 최적화되어 있다. 완전한 **비동기** 언어이며 이벤트 기반이다. 그리고 아이솔레이트를 이용한 동시성 기능도 제공해준다.
- 널 안정성, 스프레드 기능, 컬렉션 if문등 효율적으로 UI를 코딩할 수 있는 기능을 제공해준다.
- 효율적인 개발 환경을 제공해준다. 핫 리로드를 통해 코드의 변경 사항을 즉시 화면에 반영 해볼 수 있다.
- 멀티 플랫폼에서 로깅 및 디버깅을 하고 실행할 수 있다.
- AOT 컴파일이 가능하기 때문에 어떤 플랫폼에서든 빠른 속도를 자랑한다.
- 자바스크립트로의 완전한 컴파일을 지원한다.
- 백엔드 프로그래밍을 지원한다.

## 1.2 변수 선언

### 1.2.1 var

- 변수는 **var 변수명 = 값;** 형식으로 선언한다.
- 변수에 값이 들어가면 자동으로 타입을 추론해서 명시적으로 타입을 선언하지 않아도 된다.
- 실제 코드가 컴파일될 때는 추론된 타입으로 var이 치환된다.

```dart
void main(){
    var name = '상무';
    print(name);

    name = '상무상무상';
    print(name);
    // 변수명 중복은 불가능하다.
}
```

### 1.2.2 dynamic

- var 타입은 변수의 값을 사용해서 변수의 타입을 유추하는 키워드이다. 그래서 타입을 한 번 유추하면 추론된 타입이 고정된다.
- dynamic 키워드를 사용하면 변수의 타입이 고정되지 않아서 다른 타입의 값을 저장할 수 있다.

```dart
void main(){
    dynamic name = '상무';
    name = 1;
}
```

### 1.2.3 final / const

- final과 const는 변수의 값을 처음 선언 후 변경할 수 없다.
- final은 런타임, const는 빌드 타임 상수이다.
- DateTime.now()함수를 이용해보면 실행을 해봐야 값을 알 수 있는 함수여서 런타임 상수를 사용해야한다.

```dart
void main() {
    final DateTime now = DateTime.now();
    print(now);
}

void main() {
    const DateTime now = DateTime.now();  // 에러 발생
    print(now)
}
```

- 이와 같이 코드를 실행하지 않은 상태에서 값이 확정되면 const, 실행될 때 확정되면 final을 사용해줘야 한다.

### 1.2.4 변수 타입

var 키워드를 사용하면 자동으로 변수 타입을 유추할 수 있지만 직접적으로 변수 타입을 명시해주면 코드가 더 직관적이다

```dart
void main() {
  // String - 문자열
  String name = '상무야 고마워';

  // int - 정수
  int isInt = 10;

  // double - 실수
  double isDouble = 2.5;

  // bool - 불리언 (true/false)
  bool isTrue = true;
}
```

## 1.3 컬렉션

컬렉션은 여러 값을 하나의 변수에 저장할 수 있는 타입이다.

- List : 여러 값을 순서대로 저장할 때 사용한다.
- Map : 특정 키값을 기반으로 빠르게 값을 검색해야할 때 사용한다.
- Set : 중복된 데이터를 제거할 때 사용한다.
- 특징 : 서로의 타입으로 자유롭게 형변환이 가능하다 !!

### 1.3.1 List 타입

- 리스트 타입은 여러 값을 순서대로 나열한 변수에 저장할 때 사용된다.
- 리스트의 구성 단위는 원소라고 한다.
- 리스트명[인덱스] 형식으로 특정 원소에 접근할 수 있다.
- 첫 원소는 0으로 지정되고 마지막 원소는 (리스트 길이 -1) 로 지정된다.

```dart
void main() {
  // 리스트에 넣을 타입을 <> 사이에 명시할 수 있다.
  List<String> blackPinkList = ['상무', '영빈', '민수', '지웅', '알줌마'];

  print(blackPinkList);
  print(blackPinkList[0]);  // 첫 원소 지정
  print(blackPinkList[4]);  // 마지막 원소 지정

  print(blackPinkList.length);  // 길이 반환

  blackPinkList[4] = '재성';  // 3번 인덱스값 변경
  print(blackPinkList);
}
```

List 타입에는 다트 언어에서 기본으로 제공하는 함수가 많다.  
예를 들면, add() where() map() reduce()가 있다. 중요하니 꼭 짚고 넘어가자.

#### 1.3.1.1 add()

add() 함수는 List에 값을 추가할 때 사용되며 추가하고 싶은 값을 매개변수에 입력하면 된다.

```dart
void main() {
  List<String> blackPinkList = ['상무', '영빈', '민수', '지웅', '알줌마'];

  blackPinkList.add('재성'); // 리스트의 끝에 추가된다.

  print(blackPinkList);
}
```

#### 1.3.1.2 where()

where()함수는 List에 있는 값들을 순서대로 순회하면서 특정 조건에 맞는 값만 필터링 하는데 사용한다.  
매개변수에 함수를 입력해야 하며, 입력된 함수는 기존 값을 하나씩 매개변수로 입력받는다.  
순회가 끝나면 유지된 값들을 기반으로 *이터러블*이 반환된다. (이터러블이 뭔지 공부해볼 것).

```dart
void main() {
  List<String> blackPinkList = ['상무', '영빈', '민수', '지웅', '알줌마'];

  final newList = blackPinkList.where(
    (name) => name == '상무' || name == '영빈', // '상무' 또는 '영빈'만 유지
  );  // 여기서 왜 final을 썼을까? const를 쓰면 왜 안될까? 오류가 날까? DartPad에서 실습해보자.

  print(newList);
  print(newList.toList());  // Iterable을 List로 다시 변환할 때 .toList() 사용
}
```

#### 1.3.1.3 map()

map() 함수는 List에 있는 값들을 순서대로 순회하면서 값을 변경할 수 있다.  
매개변수에 함수를 입력해야 하며 입력된 함수는 기존 값을 하나씩 매개변수로 입력받는다.  
반환하는 값이 현잿값을 대체하며 순회가 끝나면 Iterable이 반환된다.
```dart
void main() {
  List<String> blackPinkList = ['상무', '영빈', '민수', '지웅', '알줌마'];

  final newBlackPink = blackPinkList.map(
    (name) => '블랙핑크 $name',  // 리스트의 모든 값 앞에 '블랙핑크' 추가
  );
  print(newBlackPink);

  // Iterable을 List로 다시 변환하고 싶을 때 .toList() 사용
  print(newBlackPink.toList());
}
```

#### 1.3.1.4 reduce()

reduce() 함수 역시 List에 있는 값들을 순회하면서 매개변수에 입력된 함수를 실행한다.  
다만 reduce()함수는 순회할 때마다 값을 쌓아가는 특징이 있다.  
지금까지 배운 함수들은 모두 Iterable을 반환했지만 reduce()함수는 List 멤버의 타입과 같은 타입을 반환한다.

```dart
void main () {
  List<String> blackPinkList = ['상무', '영빈', '민수', '지웅', '알줌마'];

  final allMembers = blackPinkList.reduce((value, element) => value + ', ' + element);

  print(allMembers);
}
```

#### 1.3.1.5 fold()

fold()함수는 reduce() 함수의 특수한 형태이다.

### 1.3.2 Map 타입

맵 타입은 키와 값의 짝을 저장한다. 순서대로 값을 저장하는 데 중점을 두는 리스트와 달리 맵은 키를 이용해서 원하는 값을 빠르게 찾는 데 중점을 둡니다.  
*Map<키 타입, 값 타입> 맵 이름* 형식으로 생성한다.

```dart
void main() {
  Map<String, String> dictionary = {
    'Harry Potter': '해리 포터',
    'Ron Weasley': '론 위즐리',
    'Hermione Granger': '헤르미온느 그레인저',
  };
  print(dictionary['Harry Potter']);
  print(dictionary['Hermione Granger']);

  print(dictionary.keys);
  print(dictionary.values);
}
```

### 1.3.3 Set 타입

셋은 중복 없는 값들의 집합이다.  
Set<타입> 세트이름 형식으로 생선한다.  
contains()함수를 사용해서 값이 있는지 없는지 확인할 수 있다.  
Set.from()을 사용하면 어떤 리스트든 Set 타입으로 변환된다.

```dart
void main() {
  Set<String> blackPink = {'상무', '영빈', '민수', '지웅', '알줌마'};

  print(blackPink.contains('알줌마'));  // 값이 있는지 확인하기
  print(blackPink.toList());  // 리스트로 변환하기

  List<String> blackPink2 = ['로제', '지수', '지수'];
  print(Set.from(blackPink2));  // List 타입을 Set 타입으로 변환
}
```

## 1.4 연산자
 ```dart
void main() {
  double number = 2;

  print(number + 2);  // 4 출력
  print(number - 2);  // 0 출력
  print(number * 2);  // 4 출력
  print(number / 2);  // 1 출력. 나눈 몫
  print(number % 2);  // 2 출력. 나눈 나머지

  // 단항 연산도 된다.
  number++;  // 3
  number--;  // 2

  number += 2;  // 4
  number -= 2;  // 0
  number *= 2;  // 4
  number /= 2;  // 1
}
 ```

### 1.4.1 null 관련 연산자
null은 아무 값도 없음을 뜻한다. 0과는 다르다 (0은 0이라는 값을 가지는 것이다.)  
다트 언어에서는 변수 타입이 null값을 가지는지 여부를 직접 지정해줘야 한다.  
타입 키워드를 그대로 사용하면 기본적으로 null값이 저장될 수 없다. 타입 뒤에 '?'를 추가해줘야 null값이 저장될 수 있다.
```dart
void main() {
  // 타입 뒤에 ?를 명시해서 null값을 가질 수 있다.
  double? number1 = 1;

  // 타입 뒤에 ?를 명시하지 않아 에러가 난다.
  double number2 = null;
}
```

타입 뒤에 ?를 추가해주면 null값이 저장될 수 있다. null을 가질 수 있는 변수에 새로운 값을 추가할 때 ??를 사용하면 기존에 null인 때만 값이 저장되도록 할 수도 있다
```dart
void main() {
  double? number;  // 자동으로 null값 지정
  print(number);

  number ??= 3;  // ??를 사용하면 기존 값이 null일 때만 저장된다.
  print(number);

  number ??= 4;
  print(number);
}
```

### 1.4.2 비교 연산자

void main() {
  int number1 = 1;
  int number2 = 2;

  // 파이썬과 동일해서 생략

  // 타입 비교 연산자
  print(number1 is int);
  print(number1 is! int);

  // 논리 연산자
  bool result = 12 > 10 && 1 > 0;  // 12가 10보다 크고 1이 0보다 클 때 (and)
  print(result);

  bool result2 = 12 > 10 || 1 > 0;  // 12가 10보다 크거나 1이 0보다 클 때 (or)
  print(result2)
}

## 1.5 제어문
제어문으로는 if, switch, while문을 제공한다

### 1.5.1 if문
if문은 원하는 조건을 기준으로 다른 코드를 실행하고 싶을 때 사용된다.

```dart
void main () {
  int number = 2;

  if (number % 3 == 0) {
    print('3의 배수입니다.');
  } else if (number % 3 == 1) {
    print('나머지가 1입니다');
  } else {
    print('맞는 조건이 없습니다');
  }
}
```

### 1.5.2 switch문
입력된 상수값에 따라 알맞은 case 블록을 수행한다.  
break 키워드를 사용하면 switch문 밖으로 나갈 수 있다.  
case 끝에 break 키워드를 사용하지 않으면 에러가 난다.  
enum과 함께 사용하면 유용하다.
```dart
enum Status {
  approved,
  pending,
  rejected,
}

void main() {
  Status status = Status.approved;

  switch (status) {
    case Status.approved:
      // approved값이기 때문에 다음 코드가 실행된다.
      print('승인 상태입니다.');
      break;
    case Status.pending:
      print('대기 상태입니다.');
      break;
    case Status.rejected:
      print('거절 상태입니다.');
      break;
    default:
      print('알 수 없는 상태입니다.');
  }

  print(Status.values)
}
```

### 1.5.3 for문
```dart
void main() {
  // 값 선언; 조건 설정; loop마다 실행할 기능
  for (int i = 0; i < 3; i++) {
    print(i);
  }

  // 다트 언어에서는 for...in 패넡의 for문도 제공해준다. 일반적으로 list의 모든 값을 순회하고 싶을 때 사용된다
  List<int> numberList = [3, 6, 9];
  for (int number in numberList) {
    print(number);
  }
}
```

### 1.5.4 while문과 do...while문
```dart
void main() {
  int total = 0;

  while(total < 10) {
    total += 1;
  }

  print(total);

  // do...while문은 반복문을 실행한 후 조건을 확인한다.
  int total1 = 0;
  
  do {
    total1 += 1;
  } while(total < 10);

  print(total);
}
```

## 1.6 함수와 람다

### 1.6.1 함수의 일반적인 특징
함수를 사용하면 한 번만 작성하고 여러 곳에서 재활용할 수 있다. 반환할 값이 없을 때는 void 키워드를 사용한다.
```dart
int addTwoNumbers(int a, int b) {
  return a + b;
}

void main() {
  print(addTwoNumbers(1, 2));
}
```
다트 함수에서 매개변수를 지정하는 방법은 두 가지가 있다.
1. 순서가 고정된 매개변수(Positional parameter)
2. 이름이 있는 매개변수(Named parameter)
포지셔널 파라미터는 입력된 순서대로 매개변수에 값이 지정된다. 예를 들어 int a 가 int b보다 먼저 선언됐기 때문에 함수를 실행할 때도 1, 2 순서대로 a와 b에 입력된다.  
이름이 있는 매개변수는 순서와 관계없이 지정하고 싶은 매개변수의 이름을 이용해 값을 입력할 수 있다. 키와 값 형태로 매개변수를 입력하면 되므로 입력 순서는 중요하지 않다.

네임드 파라미터를 지정하려면 중괄호 { }와 required 키워드를 사용해야 한다.
```dart
// required 키워드는 매개변수가 null값이 불가능한 타입이면 기본값을 지정해주거나 필수로 입력해야 한다는 의미이다.
int addTwoNumbers({
  required int a,
  required int b,
}) {
  return a + b;
}

void main() {
  print(addTwoNumbers(a: 1, b: 2));
}
```
```dart
// 기본값을 갖는 포지셔널 파라미터를 지정하려며 [] 기호를 사용하면 된다.
int addTwoNumbers(int a, [int b = 2]) {
  return a + b;
}

void main() {
  print(addTwoNumbers(1));
}

// 기본값을 갖는 네임드 파라미터를 지정하려면 required 키워드를 생략하고 등호 다음에 원하는 기본값을 입력해주면 된다.
int addTwoNumbers({
  required int a,
  int b = 2,
}) {
  return a + b;
}

void main() {
  print(addTwoNumbers(a: 1));
}

// 스까서 쓸 수도 있다.
int addTwoNumbers(
  int a, {
  required int b,
  int c = 4,
}) {
  return a + b + c;
}

void main() {
  print(addTwoNumbers(1, b: 3, c: 7));
}
```

### 1.6.2 익명 함수와 람다 함수
- 익명 함수 표현 방식 -> (매개변수) { 함수 바디 }
- 람다 함수 표현 방식 -> (매개변수) => 단 하나의 statement
익명 함수와 람다 함수의 차이는 람다 함수는 함수 로직을 수행하는 statement가 딱 하나여야한다. (한 줄이 아니고 명령 단위가 하나임.)  
람다 함수는 이름을 정하고 미리 선언할 필요가 없어서 글로벌 스코프로 다룰 필요가 없다.  
적절하게 사용하면 간결하게 코드를 작성할 수 있어서 콜백 함수나 리스트의 map, reduce, fold함수 등에서 주로 사용한다

```dart
void main() {
  List<int> numbers = [1, 2, 3, 4, 5];

  // 일반 함수로 모든 값 더하기
  final allMembers = numbers.reduce((value, element) {
    return value + element;
  })

  print(allMembers);

  // 람다 함수로 모든 값 더하기
  final allMembers = numbers.reduce((value, element) => value + element);

  print(allMembers);
}
```

### 1.6.3 typedef와 함수
typedef 키워드는 함수의 시그니처를 정의하는 값이다. 여기서 시그니처는 반환값 타입, 매개변수 개수와 타입 등을 말한다.  
즉 함수 선언부를 정의하는 키워드이다. 함수가 무슨 동작을 하는지에 대한 정의는 없다.
```dart
typedef Operation = void Function(int x, int y);
```

함수를 선언하기는 했지만 뭘하는지 동작은 없다. 그럼 이 함수를 어떻게 사용할지 알아보자.
```dart
typedef Operation = void Function(int x, int y);

void add(int x, int y) {
  print('결괏값 : ${x + y}');
}

void substract(int x, int y) {
  print('결괏값 : ${x - y}');
}

void main() {
  // typedef는 일반적인 변수의 type처럼 사용 가능하다.
  Operation oper = add;
  oper(1, 2);

  // substract() 함수도 Operation에 해당되는 시그니처이므로 oper 변수에 저장 가능하다
  oper = substract;
  oper(1, 2);
}
```
다트에서 함수는 일급 객체이므로 함수를 값처럼 사용할 수 있다. 그래서 플러터에서 typedef로 선언한 함수를 다음과 같이 매개변수로 넣어 사용한다
```dart
typedef Operation = void Function(int x, int y);

void add(int x, int y) {
  print('결괏값 : ${x + y}');
}

void calculate(int x, int y, Operation oper) {
  oper(x, y);
}

void main() {
  calculate(1, 2, add);
}
```
## 1.7 try...catch
try...catch문은 try와 catch 사이의 괄호에 에러가 없을 때 실행할 로직을 작성하고 catch가 감싸는 괄호에 에러가 났을 때 실행할 로직을 작성하면 됩니다. 만약에 try로직에서 에러가 나면 이후의 로직은 실행되지 않고 바로 catch 로직으로 넘어간다.

```dart
void main() {
  try{
    // 에러가 없을 때 실행할 로직
    final String name = '이상무';
    print(name);
  } catch(error) {
    // 에러가 있을 때 실행할 로직
    print(error);
  }
}
```


## 2.1 객체지향 프로그래밍의 시작 클래스

```dart
// class 키워드를 입력 후 클래스명을 지정해 클래스를 선언한다.
class Idol {
    // 1. 클래스에 종속되는 변수를 지정할 수 있다.
    String name = '블랙핑크';

    // 2. 클래스에 종속되는 함수를 지정할 수 있다.
    // 클래스에 종속되는 함수를 메서드라고 부른다.
    void sayName () {
        // 3. 클래스 내부의 속성을 지칭하고 싶을 때는 this키워드를 사용하면 된다.
        // 결과적으로 this.name은 Idol 클래스의 name 변수를 지칭한다.
        print('저는 ${this.name} 입니다.');
        // 4. 스코프 안에 같은 속성 이름이 하나만 존재한다면 this를 생략할 수 있다.
        print('저는 $name입니다.');
    }
}

void main() {
    // 변수 타입을 Idol로 지정
    // Idol의 인스턴스를 생성할 수 있다.
    // 인스턴스를 생성할 때는 함수를 실행하는 것처럼
    // 인스턴스화하고 싶은 클래스에 괄호를 열고 닫아준다.
    Idol blackPink = Idol();  // 1. Idol 인스턴스 생성

    // 메서드를 실행한다.
    blackPink.sayName();
}
```

### 2.1.1 생성자

- 생성자(constructor)는 클래스의 인스턴스를 생성하는 메서드이다.

```dart
class Idol {
    // 1. 생성자에서 입력받는 변수들은 일반적으로 final 키워드 사용
    // 인스턴스화한 다음에 혹시라도 변수의 값을 변경하는 실수를 막으려고.
    final String name;

    // 2. 생성자 선언
    // 클래스와 같은 이름이어야 한다.
    // 함수의 매개변수를 선언하는 것처럼 매개변수를 지정해준다.
    Idol(String name) : this.name = name;
    // Idol(this.name); 도 가능하다.

    void sayName() {
        print('저는 ${this.name} 입니다.')
    }
}

vodi main() {
    // name에 '블랙핑크' 저장
    Idol blackPink = Idol('블랙핑크');
    blackPink.sayName();

    // name에 'BTS' 저장
    Idol bts = Idol('BTS');
    bts.sayName();
}
```

### 2.2.2 네임드 생성자

네임드 생성자는 네임드 파라미터와 상당히 비슷한 개념이다.

```dart
class Idol {
    final String name;
    final int membersCount;

    // 1. 생성자
    Idol(String name, int membersCount)
        : this.name = name,
          this.membersCount = membersCount;

    // 2. 네임드 생성자
    // {클래스명.네임드 생성자명} 형식
    Idol.fromMap(Map<String, dynamic> map)
        : this.name = map['name'],
          this.membersCount = map['membersCount'];

    void sayName() {
        print('저는 ${this.name}입니다. ${this.name} 멤버는 ${this.membersCount}명입니다.')
    }

    void main() {
        // 기본 생성자 사용
        Idol blackPink = Idol('블랙핑크', 4);
        blackPink.sayName();

        // fromMap이라는 네임드 생성자 사용
        Idol bts = Idol.fromMap({'name': 'BTS', 'membersCount': 7,
        });
        bts.sayName();
    }
}
```

### 2.2.3 프라이빗 변수

다트에서의 프라이빗 변수는 다른 언어와 정의가 약간 다른게 같은 파일에서만 접근이 가능한 변수이다.

```dart
class Idol {
    // '_'로 변수명을 시작하면
    // 프라이빗 변수를 선언할 수 있다.
    String _name;

    Idol(this._name);
}

void main() {
    Idol blackPink = Idol('블랙핑크');

    // 같은 파일에서는 _name 변수에 접근할 수 있지만
    // 다른 파일에서는 _name 변수에 접근할 수 없다.
    print(blackPink._name);
}
```

2.2.4 getter / setter
게터는 값을 가져올 때 사용하고 세터는 값을 지정할 때 사용된다.

```dart
class Idol {
    String _name = '블랙핑크';

    // 1. get 키워드를 사용해서 게터임을 명시
    // 게터는 메서드와 다르게 매개변수를 전혀 받지 않는다.
    String get name {
        return this._name;
    }

    // 2. 세터는 set이라는 키워드를 사용해서 선언한다.
    // 세터는 매개변수로 딱 하나의 변수를 받을 수 있다.
    set name(String name) {
        this._name = name;
    }
}
```

## 2.2 상속

extends 키워드를 사용해 상속할 수 있다. 상속은 어떤 클래스의 기능을 다른 클래스가 사용할 수 있게 하는 기법이다.

```dart
class Idol {
    final String name;
    final int membersCount;

    Idol(this.name, this.membersCount);

    void sayName () {
        print('저는 ${this.name}입니다.');
    }

    void sayMembersCount () {
        print('${this.name} 멤버는 ${this.membersCount}명입니다.')
    }
}

// 1. extends 키워드를 사용해서 상속받는다.
// class 자식클래스 extends 부모 클래스 순서이다.
class BoyGroup extend Idol {
    // 상속받은 생성자
    BoyGroup (
        String name,
        int membersCount,
        ) : super( // super는 부모 클래스를 지칭한다.
      name,
      membersCount,
    );

    // 상속받지 않는 기능
    void sayMale() {
        print('저는 남자 아이돌입니다.');
    }
}

void main() {

    BoyGroup bts = BoyGroup('BTS', 7);  // 생성자로 객체 생성

    bts.sayName();
    bts.sayMembersCount();
    bts.sayMale();
}
```

## 2.3 오버라이드

오버라이드는 부모 클래스 또는 인터페이스에 정의된 메서드를 재정의할 때 사용된다. 다트에서는 override 키워드를 생략할 수 있기 때문에 override를 사용하지 않고도 메서드를 재정의할 수 있다.

```dart
class GirlGroup extends Idol {
    // 2.2 상속에서처럼 super 키워드를 사용해도 되고 생성자의 매개변수로 직접 super 키워드를 사용해도 된다.
    GirlGroup(
        super.name,
        super.membersCount,
    );

    @override
    void sayName() {
        print('저는 여자 아이돌 ${this.name}입니다.');
    }
}

void main() {
    GirlGroup blackPink = GirlGroup('블랙핑크', 4);

    // 1. 자식 클래스의 오버라이드된 메서드 사용
    blackPink.sayName();

    // sayMemberCount는 오버라이드하지 않았기 때문에
    // 그대로 Idol 클래스의 메서드가 실행된다.
    // 2. 부모 클래스의 메서드 사용
    blackPink.sayMembersCount();
}
```

## 2.4 인터페이스

상속은 공유되는 기능을 이어받는 개념이지만 인터페이스는 공통으로 필요한 기능을 정의만 해두는 역할을 한다. 상속은 단 하나의 클래스만 할 수 있지만 인터페이스는 적용 개수에 제한이 없다.

```dart
// 1. implements 키워드를 사용하면 원하는 클래스를 인터페이스로 사용할 수 있다.
class GirlGroup implements Idol {
    final String name;
    final int membersCount;

    GirlGroup(
        this.name,
        this.membersCount,
    );

    void sayName() {
        print('저는 여자 아이돌 ${this.name}입니다.');
    }

    void sayMembersCount() {
        print('${this.name} 멤버는 ${this.membersCount}명입니다.');
    }
}
```

## 2.5 믹스인

믹스인은 특정 클래스에 원하는 기능들만 골라 넣을 수 있는 기능이다. 특정 클래스를 지정해서 속성들을 정의할 수 있으며 지정한 클래스를 상속하는 클래스에서도 사용할 수 있다.

```dart
mixin IdolSingMixin on Idol{
  void sing(){
    print('${this.name}이 노래를 부릅니다.');
  }
}

// 믹스인을 적용할 때는 with 키워드 사용
class BoyGroup extends Idol with IdolSingMixin{
  BoyGroup(
    super.name,
    super.membersCount,
  )

  void sayMale() {
    print('저는 남자 아이돌입니다.');
  }
}

void main(){
  BoyGroup bts = BoyGroup('BTS', 7);

  // 믹스인에 정의된 sing() 함수 사용 가능
  bts.sing();
}
```

## 2.6 추상

## 2.7 제네릭

## 2.8 스태틱

## 2.9 캐스케이드 연산자

## 3.1 동기 vs 비동기

지금까지 다트 언어를 배우면서 작성한 코드는 모두 동기 방식이다. 함수를 실행하면 다음 코드가 실행되기 전에 해당 함수의 결괏값이 먼저 반환된다. 하지만 비동기 프로그래밍은 요청한 결과를 기다리지 않으며 응답 순서 또한 요청한 순서와 다를 수 있다. 그렇기 때문에 컴퓨터 자원을 낭비하지 않고 더욱 효율적으로 코드를 실행할 수 있다. 예를 들어 데이터베이스에서 게시판 글을 가져오는 작업이나, 복잡한 미적분 계산이나 이미지 인코딩 등 시간이 걸리는 작업을 동기로 실행하면 앱이 매우 느려질 수 있다. 그렇기 때문에 이런 작업은 비동기로 처리해야 한다.

## 3.2 Future
Future 클래스는 '미래'라는 단어의 의미대로 미래에 받아올 값을 뜻한다. List나 Set처럼 제네릭으로 어떤 미래의 값을 받아올지를 정할 수 있다.
```dart
 Future<String> name;  // 미래에 받을 String값
 Future<int> number;  // 미래에 받을 int값
 Future<bool> isOpened;  // 미래에 받을 boolean값
```

비동기 프로그램이은 서버 요청과 같이 오래 걸리는 작업을 기다린 후 값을 받아와야 하기 때문에 미래값을 표현하는 future 클래스가 필요하다. 특정 기간 동안 아무것도 하지 않고 기다리는 Future.delayed()를 사용해보자.

```dart
void main() {
  addNumbers(1, 1);
}

void addNumbers(int number1, int number2) {
  print('$number1 + $number2 계산 시작 !');


  // Future.delayed()를 사용하면 일정 시간 후에 콜백 함수를 실행할 수 있다.
  Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝');
}
```
코드를 실행해보면 print가 위에서 아래 순서대로 실행되지 않는다는걸 알게 된다. 하지만 Future.delayed() 함수는 비동기 연산이기 때문에 CPU가 3초간 대기해야 한다는 메시지를 받으면 리소스를 허비하지 않고 다음 코드를 바로 실행한다.  
결과적으로 CPU가 3초동안 아무것도 하지 않으며 낭비할 뻔한 시간동안 다른 작업을 할 수 있어 더 효율적으로 CPU 리소스를 사용했다.

## 3.3 async await
Future을 사용하면 코드가 작성된 순서대로는 실행이 안될 수가 있다. 그래서 async와 await를 사용하면 코드 가독성을 높일 수 있다.

```dart
void main() {
  addNumbers(1, 1);
}

// async 키워드는 함수 매개변수 정의와 바디 사이에 입력한다
Future<void> addNumbers(int number1, int number2) async {
  print('$number1 + $number2 계산 시작 !');

  // await는 대기하고 싶은 비동기 함수 앞에 입력한다.
  await Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝')
}
```
예제와 같이 함수를 async로 지정해주고 나서 대기하고 싶은 비동기 함수를 실행할 때 await 키워드를 사용하면 코드는 작성한 순서대로 실행된다.(꼭 dartpad에서 실습해봐라. 읽기만 하지 말고.) 이렇게 되면 동기 프로그래밍이라고 생각할 수 있는데 비동기 프로그래밍 특징을 유지하며 코드가 작성된 순서대로 프로그램을 실행한다.  
이해가 안간다면 실습을 하나 더 실행해보자.

```dart
void main() {
  addNumbers(1, 1);
  addNumbers(2, 2);
}

// async 키워드는 함수 매개변수 정의와 바디 사이에 입력한다
Future<void> addNumbers(int number1, int number2) async {
  print('$number1 + $number2 계산 시작 !');

  // await는 대기하고 싶은 비동기 함수 앞에 입력한다.
  await Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝')
}
```
dartpad에서 실행해보면 상당히 혼란스러운 출력 결과일 수 있다. 분석해보면 addNumbers()함수는 두 번 실행되었다. 그러니 출력 결과를 함수별로 나눠서 보면 각 addNumbers() 함수의 실행 결과가 예상한 코드 순서대로 시작되었다. 그런데 addNumbers(1, 1)가 끝나기 전에 addNumbers(2, 2)가 실행되었다. 그 이유는 addNumbers() 함수가 비동기 프로그래밍이기 때문이다. addNumbers(1, 1)의 Future.delayed()가 실행되며 3초를 기다려야 할 때 CPU의 리소스가 낭비되지 않고 바로 다음 실행할 코드인 addNumbers(2, 2)를 실행한 것이다.  

만약 addNumbers(1, 1)과 addNumbers(2, 2)가 순차적으로 실행되게 하려면 어떻게 할까?
```dart
void main() async {
  await addNumbers(1, 1);
  await addNumbers(2, 2);
}

// async 키워드는 함수 매개변수 정의와 바디 사이에 입력한다
Future<void> addNumbers(int number1, int number2) async {
  print('$number1 + $number2 계산 시작 !');

  // await는 대기하고 싶은 비동기 함수 앞에 입력한다.
  await Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝')
}
```
위의 예제같이 실행하면 된다.

### 3.3.1 결괏값 반환받기
async와 await 키워드를 사용한 함수에서도 결괏값을 받아낼 수 있다. 이때 앞서 배운 Future 클래스를 사용한다. 입력된 두 숫자를 더한 결괏값을 반환하는 addNumbers()함수의 코드를 수정해 자세히 알아보겠다.
```dart
void main() async {
  final result1 = await addNumbers(1, 1);
  print('결괏값 $result1');
  final result2 = await addNumbers(2, 2);
  print('결괏값 $result2');
}

Future<int> addNumbers(int number1, int number2) async {
  print('$number1 + $number2 계산 시작!');

  await Future.delayed(Duration(seconds: 3), (){
    print('$number1 + $number2 = ${number1 + number2}');
  });

  print('$number1 + $number2 코드 실행 끝')

  return number1 + number2;
}
```
위와 같이 await 키워드를 적용해도 일반 함수처럼 변수에 반환값을 저장하고 활용할 수 있다.
## 3.4 Stream
Future은 반환값을 딱 한 번 받아내는 비동기 프로그래밍에 주로 사용된다. 지속적으로 값을 반환 받을 때는 Stream을 사용한다. Stream은 한 번 리슨하면 Stream에 주입되는 모든 값들을 지속적으로 받아온다.

### 3.4.1 스트림 기본 사용법
스트림을 사용하려면 플러터에서 기본으로 제공하는 dart:async 패키지를 불러와야 한다. 그다음 dart:async 패키지에서 제공하는 StreamController를 listen()해야 값을 지속적으로 반환받을 수 있다.
```dart
import 'dart:async';

void main() {
  final controller = StreamController();  // StreamController 선언
  final stream = controller.stream;  // Stream 가져오기

  // Stream에 listen()함수를 실행하면 값이 주일될 때마다 콜백 함수를 실행할 수 있다.
  final streamListener1 = stream.listen((val) {
    print(val);
  });

  // Stream에 값을 주입하기
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
  controller.sink.add(4);
}
```

### 3.4.2 브로드캐스트 스트림
스트림은 단 한 번만 listen()을 실행할 수 있다. 하지만 하나의 스트림을 생성하고 여러 번 listen() 함수를 실행하고 싶을 때가 있다. 이럴 때 브로드캐스트 스트림을 사용하면 스트림을 여러 번 listen()하도록 변환할 수 있다.
```dart
import 'dart:async';

void main() {
  final controller = StreamController();

  // 여러 번 리슨할 수 있는 Broadcast Stream 객체 생성
  final stream = controller.stream.asBroadcastStream();

  // 첫 번째 listen() 함수
  final streamListener1 = stream.listen((val) {
    print('listening 1');
    print(val);
  });

  // 두 번째 listen() 함수
  final streamListener2 = stream.listen((val) {
    print('listening 2');
    print(val);
  });

  // add()를 실행할 때마다 listen()하는 모든 콜백 함수에 값이 주입된다.
  controller.sink.add(1);
  controller.sink.add(2);
  controller.sink.add(3);
}
```

### 3.4.3 함수로 스트림 반환
StreamController을 직접 사용하지 않고도 직접 스트림을 반환하는 함수를 작성할 수도 있다. Future를 반환하는 함수는 async로 함수를 선언하고 return키워드로 값을 반환하면 된다. 스트림을 반환하는 함수는 async*로 함수를 선언하고 yield 키워드로 값을 반환해주면 된다.
```dart
import 'dart:async';

// Stream을 반환하는 함수는 async*로 선언한다.
Stream<String> calcualte(int number) async* {
  for (int i = 0; i < 5; i++) {
    // StreamController의 add()처럼 yield 키워드를 이용해서 값 반환
    yield 'i = $i';
    await Future.delayed(Duration(seconds: 1));
  }
}

void playStream() {
  // StreamController와 마찬가지로 listen() 함수로 콜백 함수 입력
  calculate(1).listen((val) {
    print(val);
  });
}
void main() {
  playStream();
}
```
# 4. Dart 3.0 신규 문법

## 4.1 레코드
레코드는 포지셔널 파라미터나 레코드 파라미터 중 한 가지 방식을 적용하여 사용할 수 있다.

### 4.1.1 포지셔널 파라미터를 이용한 레코드
포지셔널 파라미터를 이용한 레코드는 포지셔널 파라미터로 표시한 타입 순서를 반드시 지켜야한다.
```dart
void main() {
  // 정확한 위치에 어떤 타입의 값이 입력될지 지정할 수 있다.
  // (String, int)는 첫 번째 값은 String 타입이고 두 번째 값은 int 타입이다.
  (String, int) sangmu = ('상무', 28);
  print(sangmu);

  // 아래와 같이 입력하면 에러가 발생한다
  (String, int) sangmu = (28, '상무');

  // 레코드의 모든 값을 사용하지 않고 특정 순서의 레코드 값을 가져오고 싶으면 '$'을 사용하면 된다.
  print(sangmu.$1);
  print(sangmu.$2);
}
```

### 4.1.2 네임드 파라미터를 이용한 레코드
네임드 파라미터는 포지셔널 파라미터와 다르게 입력 순서를 지킬 필요가 없다.  
다만 소괄호에 중괄호를 중첩하여 타입과 변수 이름을 쉼표로 구분하고 명시해줘야 한다.
```dart
void main() {
  ({String name, int age}) sangmu = (name: '상무', age: 28);

  print(sangmu);
}
```
## 4.2 구조 분해
실습해보면 이해간다.

### 4.2.1 리스트에서의 구조 분해 사용 예제
```dart
void main() {
  // 아래 코드와 같지만 구조 분해를 사용하면 한 줄에 해결할 수 있다.
  // final newJeans = ['민지', '해린'];
  // final minji = newJeans[0];
  // final haerin = newJeans[1];
  final [minji, haerin] = ['민지', '해린'];
}
```
### 4.2.2 리스트에서의 스프레드 연산자를 이용한 구조 분해 사용 예제
```dart
void main() {
  final number = [1, 2, 3, 4, 5, 6, 7, 8];

  // 스프레드 연산자를 사용하게 되면 중간의 값들을 버릴 수 있다.
  final [x, y, ..., z] = numbers;

  // 1 출력
  print(x);
  // 8 출력
  print(z);
}
```
### 4.2.3 맵에서의 구조 분해 사용 예제
```dart
void main() {
  final minjiMap = {'name': '민지', 'age': 19};
  // 위의 맵의 구조와 똑같은 구조로 구조 분해하면 된다.
  final {'name': name, 'age': age} = minjiMap;
  
  // name: 민지
  print('name: $name')''
}
```
### 4.2.4 클래스에서의 구조 분해 사용 예제
```dart
void main() {
  final minji = Idol(name: '민지', age: 19);

  // 클래스의 생성자 구조와 똑같이 구조 분해하면 된다.
  final Idol(name: name, age: age) = minji;

  // 민지 출력
  print(name);
}

class Idol {
  final String name;
  final int age;

  Idol({
    required this.name,
    required this.age,
  });
}
```
## 4.3 switch문

### 4.3.1 표현식 기능
코드는 표현식과 문으로 나눌 수 있다. 표현식은 어떠한 값을 만들어내는 코드이다.  
예를 들어 1 + 1은 값 2를 만드는 표현식이다. 이처럼 표현식이 평가되면 새로운 값을 생성하거나 기존 값을 참조한다.  

문은 기본 단위이자 가장 작은 코드 실행 단위로 명령문 즉, 컴퓨터에 내리는 명령이라고 생각하면 된다. 쉽게 말해 표현식 여러 개가 모여 문이 되며, 문에는 선언문, 할당문, 반복문 등이 있다.  
예는 var a = 3 처럼 값을 할당하는 코드이다. 다트 3.0부터는 swtich문을 함수처럼 사용하여 직접 값을 반홚받을 수 있는 절 기능이 추가되었다.
```dart
void main() {
  String dayKor = '월요일';

  // switchㅁ눈이 함수처럼 값을 반환한다.
  String dayEnglish = switch (dayKor) {
    // '=>'를 사용하면 switch문 조건에 맞을 때 값을 반환할 수 있다.
    '월요일' => 'Monday',
    '화요일' => 'Tuesday',
    '수요일' => 'Wednesday',
    '목요일' => 'Thursday',
    '금요일' => 'Friday',
    '토요일' => 'Saturday',
    '일요일' => 'Sunday',
    // _는 default와 같은 의미로 사용된다.
    _ => 'Not Found',
  };

  print(dayEnglish);
}
```
### 4.3.2 패턴 매칭
```dart
void switcher(dynamic anything) {
  switch (anything) {
    // 정확히 'aaa' 문자열만 매치한다.
    case 'aaa':
      print('match: aaa');
      break;
    // 정확히 [1, 2] 리스트만 매치한다.
    case [1, 2]:
      print('match: [1, 2]');
      break;
    // 3개의 값이 들어 있는 리스트를 모두 매치한다.
    case [_, _, _]:
      print('match: [_, _, _]');
      break;
    // 첫 번째와 두 번째 값에 int가 입력된 리스트를 매치한다.
    case [int a, int b]:
      print('match: [int $a, int $b]');
      break;
    // 첫 번째 값에 String, 두 번째 값에 int가 입력된 record 타입을 매치한다.
    case (String a, int b):
      print('match: (String: $a, int: $b)');
      break;
    default:
      print('no match');
  }
}

void main() {
  switcher('aaa');
  switcher([1, 2]);
  switcher([3, 4, 5]);
  switcher([6, 7]);
  switcher(('민지', 19));
  switcher(8);
}
```
### 4.3.3 엄격한 검사
엄격한 검사는 코드가 입력받을 수 있는 모든 조건을 전부 확인하고 있는지 체크하는 기술이다.
```dart
void main() {
  // val에 입력될 수 있는 값은 true, false, null이다.
  bool? val;

  // null 조건을 입력하지 않았기 때문에 non exbaustive switch statement 에러가 나온다.
  // null case를 추가하거나 default case를 추가해야한다.
  switch(val) {
    case true:
      print('true');
    case false:
      print('false');
  };
};
```
### 4.3.4 보호 구문
switch문에는 when 키워드로 보호 구문을 추가할 수 있또록 업데이트 됐다. when 키워드는 boolean으로 반환할 조건을 각 case문에 추가할 수 있으며 when 키워드 뒤에 오는 조건이 true를 반환하지 않으면 case 매치가 안된다.
```dart
void main() {
  (int a, int b) val = (1, -1);

  // default가 출력된다. 만약에 b 값을 0 이상으로 변경하면 1, _를 출력할 수 있따.
  switch (val) {
    case (1, _) when val.$2 ? 0:
      print('1, _');
      break;
    default:
      print('default');
  }
}
```
## 4.4 클래스 제한자

### 4.4.1 base 제한자

### 4.4.2 final 제한자

### 4.4.3 interface 제한자

### 4.4.4 sealed 제한자

### 4.4.5 mixin 제한자

## 5.1 플러터 소개

플러터는 구글이 구현한 크로스 플랫폼 프레임워크이다. 플러터는 스키아엔진이라는 2D 렌더링 엔진과 직접 통신을 하기 때문에 스키아 엔진이 실행되는 플랫폼에서는 똑같은 API를 사용해서 프로그래밍할 수 있다.

- 플러터 계층 구조
  - 임베더 계층
    - 임베더는 플러터가 현재 지원하는 6개 플랫폼의 네이티브 플랫폼과 직접 통신을 하고 운영체제의 자체적 기능을 모듈화해둔 계층이다. 이 모듈들은 각 플랫폼의 네이티브 언어로 작성되어 있다.
  - 엔진 계층
    - 이 계층은 대부분 C++로 작성되어 있으며 플러터 코어 API와 스키아 그래픽 엔진, 파일시스템 그리고 네트워크 기능 등이 정의돼 있다.
  - 프레임워크 계층
    - 플러터 프레임워크를 사용하는 데 필수적인 위젯, 애니메이션, 머티리얼 패키치, 쿠퍼티노 패키지 등이 있다.

## 6.1 위젯 소개

'Everything is a Widget'은 구글에서 플러터에서 소개하는 문구이다. 플러터에서 화면에 보여지는 UI와 관련된 모든 요소는 위젯으로 구성되어 있다. 위젯은 현재 주어진 상태(데이터)를 기반으로 어떤 UI를 구현할지를 정의한다. 위젯의 상태가 변경되면 변경 사항에 알맞게 변경된 UI를 화면에 다시 그려준다. 이때 플러터 프레임워크는 기존 상태의 위젯과 새로운 상태의 위젯을 비교해서 UI 변화를 반영할 때 필요한 최소한의 변경 사항을 산출해서 화면을 그려낸다. 결과적으로 플러터는 최소한의 리소스를 이용해서 UI 변경을 이끌어낼 수 있으며, 최대 120FPS까지 높은 퍼포먼스를 발휘할 수 있다.

위젯은 자식을 하나만 갖는 위젯과 자식을 여럿 갖는 위젯으로 나뉜다. 자식을 하나만 갖는 대표적인 위젯들은 다음과 같으며 대체로 child매개변수를 입력받는다

- Container 위젯 : 자식을 담는 컨테이너 역할을 한다. 다만 단순하게 자식을 담는 역할을 하는 게 아니라 배경색, 너비와 높이, 테두리 등의 디자인을 지정할 수 있다.
- GestureDetector 위젯 : 플러터에서 제공하는 제스처 기능을 자식 위젯에서 인식하는 위젯이다. 탭이나 드래그 그리고 더블 클릭 같은 제스처 기능이 자식 위젯에 인식됐을 때 함수를 실행할 수 있다
- SizedBox 위젯 : 높이와 너비를 지정하는 위젯이다. Container 위젯과 다르게 디자인적 요소는 적용할 수 없고 const 생성자로 선언할 수 있어서 퍼포먼스 측면에서 더 효율적이다.

다수의 자식을 입력할 수 있는 위젯은 children 매개변수를 입력받으며 리스트로 여러 위젯을 입력할 수 있다. 대표적인 다수의 자식을 입력할 수 있는 위젯은 아래와 같다.

- Column 위젯 : children 매개변수에 입력된 모든 위젯들을 세로로 배치한다.
- Row 위젯 : children 매개변수에 입력된 모든 위젯들을 가로로 배치
- ListView 위젯 : 리스트를 구현할 때 사용합니다. 마찬가지로 children 매개변수에 다수의 위젯을 입력할 수 있으며 입력된 위젯이 화면을 벗어나게 되면 스크롤이 가능해진다.

```dart
// 실습용 템플릿
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
            child:  // 1. 예제 코드 작성 라인
        ),
      ),
    );
  }
}
```

## 6.2 텍스트 관련 위젯

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
            child: Text(
          // 작성하고 싶은 글
          '이상무짱짱맨',
          // 글자에 style 적용
          style: TextStyle(
            fontSize: 24.0,
            fontWeight: FontWeight.w700,
            color: Colors.blue,
          ),
        )),
      ),
    );
  }
}

```

## 6.3 버튼 관련 위젯

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // const 제거
      // 여기서 왜 !! const를 쓰면 실행이 안될까?
      // TextButton 내부의 style이나 onPressed 속성 등이 컴파일 타임에 결정될 수 없는 동적 값이기 때문에 const를 사용할 수 없다.
      home: Scaffold(
        body: Center(
          child: TextButton(
            onPressed: () {
              // 버튼이 눌렸을 때 수행할 동작
            },
            style: TextButton.styleFrom(
              foregroundColor: Colors.red,
            ),
            child: const Text('텍스트 버튼'),
          ),
        ),
      ),
    );
  }
}

```

이 외에도 IconButton 위젯, GestureDetector 위젯,Container 위젯, SizedBox 등등 엄청 다양한 위젯이 있는데 너무 많기 때문에 직접 찾아보길 바란다.

# 2024 09 05에 이상무에 의해 작성된 문서입니다. 추가 학습을 해서 비어있는 부분을 채우거나 실습을 더 진행해봅시다 !