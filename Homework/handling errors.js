function parseUserInput(input) {
    try {
        let parse = JSON.parse(input);
        console.log("Valid JSON:", parsed);
    }
    catch (error){
        console.log("Invalid JSON! Error:", error.message);
    }
    finally {
        console.log("Validation complete.");
    }
}
parseUserInput('{"name": "Alice"}');
parseUserInput("This is not JSON")
