function multiplynum(num1, num2) {
    return num1 * num2;
}

function multiplication(a, b){
    let num1 = parseFloat("Enter the first number you would like to multiply")
    let num2 = parseFloat("Enter the second number you would like to multiply")
    let result = multiplynum(a, b);
    console.log(`The result of multiplying ${a} and ${b} is: ${result}`);
}

