class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  displayInfo() {
    return `Name: ${this.name}, Age: ${this.age}`;
  }

  static greet() {
    return "Hello! I am a person.";
  }
}

class Student extends Person {
  constructor(name, age, grade) {
    super(name, age); 
    this.grade = grade;
  }

  displayStudentInfo() {
    return `${this.displayInfo()}, Grade: ${this.grade}`;
  }
}

console.log(Person.greet()); 

const student1 = new Student("Mahir", 20, "A");

console.log(student1.displayStudentInfo());

