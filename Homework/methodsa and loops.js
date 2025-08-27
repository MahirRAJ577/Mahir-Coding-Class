let now = new Date();
console.log(now.toLocaleDateString());  
console.log(now.toLocaleTimeString());  
console.log(now.toLocaleString());      

function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function printRandomNumbers(option) {
    let option = parseInt(prompt("Choose an option:\n1. Print 5 numbers\n2. Print 10 numbers\n3. Print 15 numbers"));

    let count;

    switch (option) {
    case 1:
      count = 5;
      break;
    case 2:
      count = 10;
      break;
    case 3:
      count = 15;
      break;
    default:
      alert("Invalid option! Defaulting to 5 numbers.");
      count = 5;
  }

  let min = parseInt(prompt("Enter minimum number:"));
  let max = parseInt(prompt("Enter maximum number:"));

  if (isNaN(min) || isNaN(max) || min >= max) {
    alert("Invalid range! Defaulting to 1 - 100.");
    min = 1;
    max = 100;
  }

  console.log(`Printing ${count} random numbers between ${min} and ${max}:`);

  for (let i = 0; i < count; i++) {
    console.log(generateRandomNumber(min, max));
  }
}

printRandomNumbers();