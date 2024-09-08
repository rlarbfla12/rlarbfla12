// 1. 묵시적 형변환 -> 자바스크립트가 알아서
let num = 10;
let str = "20";

const result = num + str;
console.log(result)

// 2. 명시적 형변환 -> 우리가 내장함수 등을 이용해 직접 형변환을 명시
// 문자열 -> 숫자
let str1 = "10";
let str1ToNum1 = Number(str1);
console.log(10 + str1ToNum1)

let str2 = "10개";
let str2ToNum2 = parseInt(str2)
console.log(str2ToNum2)


// 숫자 -> 문자열
let num1 = 20;
let num1Tostr1 = String(num1);
console.log(num1Tostr1 + "입니다.")

// 삼항 연산자
let var8 = 8;
let res = var8 % 2 === 0 ? "짝수" : "홀수";
console.log(res)