function validate(e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const messagebox = document.getElementById("message").value;

    let message = "";

    if(email === "") {
        message = "Please enter an email";
        messagebox.style.color = "red";
    }
    else if(pass === "") {
        message = "Please enter an password";
        messagebox.style.color = "red";
    }
    else if(age === "") {
        message = "Age must be between 12 and 50";
        messagebox.style.color = "red";
    }
    else {
        message = "Log in success";
        messagebox.style.color = "green";
    }
}