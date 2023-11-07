//a.
function getAvgGrade(grades, name) {
    const sumGrades = grades.reduce((sum, value) => sum + value, 0);
    avgGrade = sumGrades/ grades.length;
    let counter = name.match(/[auieo]/ig).length;
    return avgGrade + counter;
}

const student1 = {
    name: "Spongebob", 
    age: 19, 
    grades: [89, 45, 100, 44, 87], 
    avgGrades: function() {return getAvgGrade(this.grades, this.name)}
};

const student2 = {
    name: "Patrick", 
    age: 15, 
    grades: [9, 95, 10, 94, 37], 
    avgGrades: function() {return getAvgGrade(this.grades, this.name)}
};

const student3 = {
    name: "Squidward", 
    age: 29, 
    grades: [92, 24, 60, 49, 78], 
    avgGrades: function() {return getAvgGrade(this.grades, this.name)}
};

const student4 = {
    name: "Mr. Krab", 
    age: 20, 
    grades: [54, 11, 100, 38, 91], 
    avgGrades: function() {return getAvgGrade(this.grades, this.name)}
};

const student5 = {
    name: "Perl", 
    age: 12, 
    grades: [1, 99, 69, 20, 77], 
    avgGrades: function() {return getAvgGrade(this.grades, this.name)}
};
//b
const students = [student1, student2, student3, student4, student5];
//c.
students.forEach((_, index) => console.log(index));
students.forEach((student) => console.log(`Student Name: ${student.name}\nAge: ${student.age}\nGrades: ${student.grades}\nAverage Grades: ${student.avgGrades()}\n`));

//d.
function getAdults(students){
    let adults = [];
    adults = students.filter((student) => student.age >= 18);
    return adults;
}
console.log(getAdults(students));

//e. 
function getAgeCar(year){
    return new Date().getFullYear() - year;
}

const myCar1 = {
    company: "Toyota",
    model: "Corola",
    year: 2020,
    carAge: function() {return getAgeCar(this.year)}
};

const myCar2 = {
    company: "Kia",
    model: "Sportage",
    year: 2008,
    carAge: function() {return getAgeCar(this.year)}
};

const myCar3 = {
    company: "Tesla",
    model: "New",
    year: 2022,
    carAge: function() {return getAgeCar(this.year)}
};
const myCars = [myCar1, myCar2, myCar3];
myCars.forEach((car) => console.log(`Car Company: ${car.company}\nModel: ${car.model}\nYear: ${car.year}\nCar Age: ${car.carAge()}\n`));
