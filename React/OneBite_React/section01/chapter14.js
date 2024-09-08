// 스코프

let a = 1 // 전역스코프

function funA() {
    let b = 2; // 지역스코프
    console.log(a);
}

funA();
// console.log(b);


// 객체
let person = {
    name : "김규림",
    age : 27,
    hobby : "피자먹기",
};

// 프로퍼티 접근
let name = person.name;
console.log(name);
let age = person["age"]
console.log(age);

// 프로퍼티 추가
person.job = "fe developer";
person["favoriteFood"] = "로제찜닭";
console.log(person);


// 프로퍼티 수정
person.job = 'edutator';
person["favoriteFood"] = "초콜릿";
console.log(person);

// 프로퍼티 삭제
delete person.job;
console.log(person);

// 프로퍼티 존재 유무 (in 연산자)
let result1 = "name" in person;
console.log(result1);


// 상수 객체
const animal = {
    type : "고양이",
    name : "나비",
    color : "black",
};

animal.age = 2;
animal.name ="까망이";
delete animal.color;
console.log(animal);


// 메서드 -> 값이 함수인 프로터피
let person2 = {
    name : "김규림",
    sayhi :  () => {
        console.log("안녕하세요");
    },
};

person2.sayhi();


// 베열
// 객체와 다른점: 배열은 순차적임

// 배열 생성
let arrC = [1, 2, 3, true, "hi", null];
console.log(arrC);

// 배열의 원소에 접근
let item1 = arrC[1];
let item2 = arrC[0];

arrC[0] = "푸하하!";
console.log(arrC);

// 