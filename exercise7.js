const friends_arr = ["sandy", "patrick", "squidward", "Mr. krabs", "gary"];
console.log(friends_arr);
console.log(friends_arr.length);
friends_arr.push("Mrs. puff");
console.log(friends_arr);
console.log(friends_arr.length);
friends_arr[0] = "Pearl";
console.log(friends_arr);

/*A const array can be edited (you can add new elements and change the elements in the array). However it cannot be reassigned to 
another array, so this example: friends_arr = ["hey"]; won't work. the const key name applies to the reference to the variable and not the
variable itself, so you can change its content but not its reference. */