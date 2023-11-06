function evalNumbers(first_num, second_num, math_func){
    let text;
    let result
    switch (math_func){
        case "add":
            text = "Sum";
            result = first_num + second_num;
            break;
        case "subtract":
            text = "Difference";
            result = Math.abs(first_num - second_num);
            break;
        case "multiply":
            text = "Product";
            result = first_num * second_num;
            break;
        case "divide":
            text = "Division";
            result = first_num / second_num;
            break;
        case "modulus":
            text = "Modulus";
            result = first_num % second_num;
            break;
        default:
            text =  "invalid input";
    }
    if (text != "invalid input")
        console.log(`${text} of ${first_num} and ${second_num} is ${result} `)
    else
        console.log(`${text}`)
}


evalNumbers(15, 10, "add")
evalNumbers(20, 8, "subtract")
evalNumbers(12, 4, "multiply")
evalNumbers(28, 7, "divide")
evalNumbers(22, 3, "modulus")
evalNumbers(33, 4, "fff")
