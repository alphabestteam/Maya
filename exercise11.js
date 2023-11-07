//1.
const helloWorld = () => "Hello World";

//2.
const sayHi = (name) => `Hello ${name}`;

//3.
const setSquared = (num) => num ** 2;

//4.
const rectangleArea = (first_num, second_num) => first_num * second_num;

//5.
const circleValues = (radius) => [2 * Math.PI *radius, Math.PI * radius ** 2];

//6.
const countVowels = (str) => {
    let counter = 0;
    for (char of str.toLowerCase()){
        if ('aeiou'.includes(char))
            counter++;
    }
    return counter;
}

//7.
const isSameLength = (first_arr, second_arr) => first_arr.length === second_arr.length;

//8.
const numberToArray = (num) => num.toString().split("").map(Number);

//9.
const getTruthyFalsyArr = (arr) => arr.map(element => Boolean(element));

console.log(helloWorld());
console.log(sayHi("Maya"));
console.log(setSquared(4));
console.log(rectangleArea(5, 6));
console.log(circleValues(1));
console.log(countVowels("May the Force be with you. Always"));
console.log(isSameLength([1, 2, 3, 4], ["3", "aaa", "b", "q"]));
console.log(numberToArray(12345));
console.log(getTruthyFalsyArr([1, "hello", true, 0, false, "", " ", null, undefined, NaN, 2,
 "world", true, {}, [], 3, "foo", 'true', 'false', "bar"]));



