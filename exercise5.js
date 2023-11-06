function check_grade(grade){
    let letter_grade;
    if (grade == 100)
        letter_grade = "A+"
    else if (grade <= 99 && grade >= 90) 
        letter_grade = "A"
    else if (grade <= 89 && grade >= 80) 
        letter_grade = "B"
    else if (grade <= 79 && grade >= 70) 
        letter_grade = "C"
    else if (grade <= 69 && grade >= 60) 
        letter_grade = "D"
    else if (grade <= 59 && grade >= 50) 
        letter_grade = "E"
    else if (grade <= 49 && grade >= 0) 
        letter_grade = "F"
    else
        return "invalid input!"

    let text;
    switch (letter_grade){
        case "A+":
            text = "Perfect"
            break;
        case "A":
            text = "Amazing"
            break;
        case "B":
            text = "Nicely done"
            break;
        case "C":
            text = "This is fine"
            break;
        case "D":
            text = "You can do better"
            break;
        case "E":
            text = "Moed B is an option"
            break;
        default:
            text = "Moed B is a must"
    }
    return `${text}!`
}
let input_field = document.createElement("input")
input_field.type = "number"
input_field.placeholder = "Please enter a valid grade!"

let btn_grade_me = document.createElement("button");
btn_grade_me.innerHTML = "Check Grade";

let result_display = document.createElement("p");

btn_grade_me.addEventListener("click", function() {
    let grade_result = check_grade(parseInt(input_field.value));
    result_display.textContent = grade_result;
})

document.body.appendChild(input_field);
document.body.appendChild(btn_grade_me);
document.body.appendChild(result_display);