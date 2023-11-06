//----------EXERCISE 8----------
//1.
/* The difference between arr[index] and arr.at(index), is that the at() method is a newer method, and it allows you to use 
negative values as index as well, and when it does that it goes from the end to the start, but if you put a negative index in the
arr[index] method, it will return undefined. the arr.at(-1) method is cleaner than writing arr[arr.length - 1]*/

//2.
function create_arr(input_char, input_num){
    let text = "";
    console.log(text.padStart(input_num, input_char).split(""));
}

//3.
function remove_last_elements(input_arr, input_num){
    if (input_arr.length >= input_num){
        input_arr.splice(-input_num);
        console.log(input_arr);}
    else
        console.log("The number is higher than the length of the array!");
}

//4.
function add_to_start_arr(input_arr, input_num){
    input_arr.unshift(input_num);
    console.log(input_arr);
}

//5.
function join_two_arrs(first_array, second_array){
    console.log(first_array.concat(second_array));
}

//6.
function convert_to_upper_case(str_arr){
    let upper_case_arr = str_arr.map((str) => str.toUpperCase());
    console.log(upper_case_arr);
}

//7.
function get_double_digits(input_arr){
    arr_num = input_arr.filter((num) => num.toString().length == 2);
    console.log(arr_num);
}

//8.
function is_value_in_arr(input_arr, value){
    console.log(input_arr.includes(value));
}

//9.
function bigger_than_ten(input_arr){
    return input_arr.find((num) => num > 10);
}

//10.
function bigger_than_ten_exits(input_arr){
    return bigger_than_ten(input_arr) != undefined;
}

//11.
/*sort(), sorts an array with strings, and each value that its data type is not string, it turns it to string and sorts it, and so 
with numbers, it turns them into strings and takes the first digit(just like it would take the first letter in a word) and checks what comes first
and 1 comes before two so if you have 10 and 2 it will sort the 10 before the 2 because it looks at the first digit.*/

//12. 
function sort_number(input_arr){
    input_arr.sort(function(a, b){return a - b});
    return input_arr;
}

//13.
function stars_to_arr(input_arr){
    const sorted_arr = sort_number(input_arr);
    const str_stars = sorted_arr.join("**")
    console.log(str_stars)

}

//14.
function sort_alphabetically(input_arr){
    input_arr.sort(function(a,b){
        let x = a.toLowerCase();
        let y = b.toLowerCase();
        if (x > y) {return 1;}
        if (x < y) {return -1;}
        return 0;
    })
    console.log(input_arr);
}

//15.
function are_all_elements_smaller(input_arr, threshold_value){
    let are_elements_smaller = input_arr.every(compare_nums.bind(threshold_value));
    console.log(are_elements_smaller)
}

function compare_nums(value){
    return value < this
}

//16.
function is_element_bigger(input_arr, input_num){
    let is_element_smaller = input_arr.some(bigger_element.bind(input_num));
    console.log(is_element_smaller)
}

function bigger_element(value){
    return value > this
}

create_arr("A", 3);
remove_last_elements([4,5,2,4], 2);
add_to_start_arr([3,4,5,6],2);
join_two_arrs([2,4,6], [2,1,1,1]);
convert_to_upper_case(["hello", "name", "maya"]);
get_double_digits([3, 59, 303, 55, 12, 2]);
is_value_in_arr([3,4,5,2,3], 1);
console.log(bigger_than_ten([3, 51, 2, 44, 1, 4]));
console.log(bigger_than_ten_exits([3, 51, 2, 44, 1, 4]));
console.log(sort_number([34, 1, 23, 2222, 1, 49, 56]));
stars_to_arr([34, 1, 23, 2222, 1, 49, 56]);
sort_alphabetically(["maya", "hod", "HELLO", "No"]);
are_all_elements_smaller([3,5,1,2], 10);
is_element_bigger([3,3,331,2], 10);
