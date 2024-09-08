// 함수 선언

function greeting () {
    console.log("안녕하세요")
}

greeting();


// 직사각형 구하기
function getArea (width, height) {
    // let width = 10;
    // let height = 20;
    let area = width * height;
    return area
}

let area1 = getArea(10, 20);
console.log(area1)
getArea(30, 20);



//  함수 표현식
function funcA () {
    console.log("funcA");
}

let varA = funcA;
varA();

let varB = function () {
    console.log("funcB")
}

varB() ;

// 화살표함수

let varC =  (value) => {
    return value + 1;
}
console.log(varC(10));


// 콜백함수
function main(value) {
    // console.log(value);
    value();
}

// function sub () {
//     console.log("i am sub");
// }

// main(sub);

main( () => {
    console.log("i am sub");
});



// 콜백함수 활용
function repeat (count, callback) {
    for (let idx = 1 ;  idx <= count ; idx++) {
        callback(idx);
        
    } 
}

// function repeatDouble (count) {
//     for (let idx = 1 ;  idx <= count ; idx++) {
//         console.log(idx * 2);
//     } 
// }

repeat(5,  (idx) => {
    console.log(idx)
});
repeat(5,  (idx) => {
    console.log(idx*2)
});
// repeatDouble(5);