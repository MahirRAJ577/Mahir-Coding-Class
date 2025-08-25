function multiplyNumbers(a, b) {
    return a * b;
}

function performMultiplication() {
    let num1 = parseFloat(prompt("Enter the first number:"));
    let num2 = parseFloat(prompt("Enter the second number:"));

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numbers!");
        return;
    }

    let result = multiplyNumbers(num1, num2);
    alert(`The result of multiplying ${num1} and ${num2} is: ${result}`);
}

performMultiplication();
