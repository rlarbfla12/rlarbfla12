// if문

let num = 10;
if (num >= 10) {
    console.log("num은 10이상입니다.");
} else if (num >= 5) {
    console.log("5이상이네~")
} else {
    console.log("10이하지롱")
}

// swith문 (break 필수)
// 다수의 조건을 처리할 때 if 보다 더 직관적

let animal = "tiger";

switch (animal) {
    case "cat": {
        console.log("고양이");
        break;
    }
        case "dog": {
        console.log("강아지");
        break;

        }
            case "bear": {
        console.log("곰");
        break;

            }
                case "snake": {
        console.log("뱀");
        break;

                }
                default:{
                    console.log("그런 동물 모름")
                }
}

