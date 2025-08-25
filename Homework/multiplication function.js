function multiplynum(num1, num2) {
    return num1 * num2;
}

function multiplication(a, b){
    let result = multiplynum(a, b);
    console.log(`The result of multiplying ${a} and ${b} is: ${result}`);
}

let num1 = prompt("Enter the first number you would like to multiply")
let num2 = prompt("Enter the second number you would like to multiply")