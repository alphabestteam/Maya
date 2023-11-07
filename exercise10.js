let newMap = new Map([])
    newMap.set("Main character", "spongebob"); 
    newMap.set("Best friend", "partick");
    newMap.set("pet", "gary");
    newMap.set("word buddy", "squidward");
    newMap.set("manager", "Mr. Krabs");
    newMap.set("teacher", "Mrs. Puff");
    newMap.set("location", "bikini bottom");



//1.
console.log(newMap);

//2.
console.log(Array.from(newMap.keys()));

//3.
console.log(newMap.get("location"));

//4. 
console.log(newMap.size)

//5. 
newMap.delete("location")

//6.
console.log(newMap.size)

//7.
console.log(newMap);

//8.
console.log(newMap.has("location"))