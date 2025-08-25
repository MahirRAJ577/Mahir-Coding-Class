function getRandomNumber() {
    return new Promise((resolve) => {
        setTimeout(() => {
            const randomNumber = Math.floor(Math.random() * 100) + 1;
            resolve(randomNumber);
        }, 1000); 
    });
}

async function printRandomNumbers(count) {
    let i = 0;
    while (i < count) {
        const number = await getRandomNumber();
        console.log(`Random number ${i + 1}: ${number}`);
        i++;
    }
}
printRandomNumbers(5);